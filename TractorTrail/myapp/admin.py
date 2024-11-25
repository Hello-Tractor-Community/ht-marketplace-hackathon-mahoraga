from django.contrib import admin
from .models import TractorListing, Contact, Dealer

# Register your models here.
admin.site.register(Contact)
admin.site.register(TractorListing)
admin.site.register(Dealer)
