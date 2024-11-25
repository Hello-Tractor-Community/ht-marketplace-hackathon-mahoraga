from django import forms
from django.contrib.auth.models import User
from .models import Seller
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']  # Include any fields you want to be editable

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['business_name', 'contact_number', 'address']

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['profile_picture']
