from django.contrib import admin

from checkout_kata.models import Product, Offer, Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(Offer)
admin.site.register(Cart)