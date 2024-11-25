from django.contrib.auth import login
from django.shortcuts import render, redirect

from . import models
from .forms import UserRegistrationForm, SellerRegistrationForm, ProductForm
from .models import Seller, Product, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Product, ProductView
from django.shortcuts import get_object_or_404

def homepage(request):
    return render(request, 'loaders/homepage.html')

def register_seller(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        seller_form = SellerRegistrationForm(request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegistrationForm()
        seller_form = SellerRegistrationForm()
    return render(request, 'loaders/register_seller.html', {'user_form': user_form, 'seller_form': seller_form})

@login_required
def seller_dashboard(request):
    if not hasattr(request.user, 'seller'):
        return redirect('register_seller')

    seller = request.user.seller
    query = request.GET.get('q')
    products = Product.objects.filter(seller=seller)

    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)

        # Store the query in recent searches
        recent_searches = request.session.get('recent_searches', [])
        if query not in recent_searches:
            recent_searches.insert(0, query)  # Add new search to the beginning
            recent_searches = recent_searches[:5]  # Keep only the last 5 searches
        request.session['recent_searches'] = recent_searches  # Save back to session

    # Retrieve recent searches from the session
    recent_searches = request.session.get('recent_searches', [])

    # Get today's date and calculate the last month and year
    today = timezone.now()
    last_month = today - datetime.timedelta(days=30)
    last_year = today - datetime.timedelta(days=365)

    # Aggregate metrics
    total_views_last_month = 0
    total_sales_last_month = 0
    total_sales_last_year = 0

    for product in products:
        product.views_last_month = product.views.filter(view_date__gte=last_month).count()
        product.views_last_year = product.views.filter(view_date__gte=last_year).count()
        product.sales_last_month = product.orders.filter(order_date__gte=last_month).aggregate(Sum('total_price'))['total_price__sum'] or 0
        product.sales_last_year = product.orders.filter(order_date__gte=last_year).aggregate(Sum('total_price'))['total_price__sum'] or 0

        # Aggregate totals
        total_views_last_month += product.views_last_month
        total_sales_last_month += product.sales_last_month
        total_sales_last_year += product.sales_last_year

    # Pass the first product's metrics if products exist
    first_product = products.first()

    return render(request, 'loaders/seller_dashboard.html', {
        'seller': seller,
        'products': products,
        'orders': Order.objects.filter(product__seller=seller),
        'total_views_last_month': total_views_last_month,
        'total_sales_last_month': total_sales_last_month,
        'total_sales_last_year': total_sales_last_year,
        'first_product': first_product,
        'query': query,# Pass the first product explicitly
        'recent_searches': recent_searches,
    })


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm()
    return render(request, 'loaders/add_product.html', {'form': form})

def track_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    ProductView.objects.create(product=product, customer_ip=request.META.get('REMOTE_ADDR'))
    return HttpResponse('Product view tracked')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user.seller)  # Ensure the product belongs to the logged-in seller

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)  # Pre-fill the form with the product data
        if form.is_valid():
            form.save()  # Save changes to the product
            return redirect('seller_dashboard')  # Redirect to dashboard after editing
    else:
        form = ProductForm(instance=product)  # Populate the form with existing product data

    return render(request, 'loaders/edit_product.html', {'form': form, 'product': product})


# @login_required
# def edit_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id, seller=request.user.seller)
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Product "{product.name}" has been updated successfully!')
#             return redirect('seller_dashboard')
#     else:
#         form = ProductForm(instance=product)
#
#     return render(request, 'loaders/edit_product.html', {'form': form, 'product': product})

