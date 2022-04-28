from django.contrib import admin

from .models import ProductsList

# Register your models here.

class ProductsListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('GTIN', {'fields': ['gtin']}),
        ('Date', {'fields':['expiry_date']})
        ]
    list_display = ('gtin', 'expiry_date')
    list_filter = ['expiry_date']

admin.site.register(ProductsList, ProductsListAdmin)