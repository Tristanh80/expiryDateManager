from django.contrib import admin

from .models import ProductsList

# Register your models here.

class ProductsListAdmin(admin.ModelAdmin):
    fields = ['gtin', 'expiry_date']

admin.site.register(ProductsList, ProductsListAdmin)