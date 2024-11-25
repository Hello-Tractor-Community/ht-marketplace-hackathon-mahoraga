from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Contact, Dealer
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def about(request):
    return render(request, 'about.html')



def admin_required(view_func):
    return user_passes_test(lambda u: u.is_staff, login_url='/admin/login/')(view_func)




def about(request):
    if request.method == "POST":
        tocontact= Contact(
            name = request.POST['fullname'],
            email = request.POST['email'],
            phonenumber = request.POST['phonenumber'],
            subject =  request.POST['subject'],
            message = request.POST['message'],
        )
        tocontact.save()
        
        return redirect('/about')
    else:
        return render(request, 'about.html')

def dealer_list(request):
    dealers = Dealer.objects.all()  # Fetch all dealers from the database
    context = {
        'dealers': dealers
    }
    return render(request, 'dealers.html', context)


