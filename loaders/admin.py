from django.contrib import admin
from .models import Seller, Product, Order

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Order)