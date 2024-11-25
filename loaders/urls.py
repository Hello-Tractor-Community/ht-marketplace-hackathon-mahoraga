from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Root URL
    path('register/', views.register_seller, name='register_seller'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('login/', auth_views.LoginView.as_view(template_name='loaders/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
