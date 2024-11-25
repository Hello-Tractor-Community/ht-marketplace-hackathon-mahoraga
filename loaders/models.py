from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png')

    def __str__(self):
        return self.business_name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    total_sales = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_email = models.EmailField()

    def __str__(self):
        return f"Order for {self.product.name} by {self.customer_email}"


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='views')
    view_date = models.DateTimeField(auto_now_add=True)
    customer_ip = models.CharField(max_length=15)  # Track customer IP or any other identifier

    def __str__(self):
        return f"View for {self.product.name} at {self.view_date}"

