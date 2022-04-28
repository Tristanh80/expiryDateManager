from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import ProductsList

# Create your views here.

class ProductsView(generic.ListView):
    template_name = 'date/index.html'
    context_object_name = 'product_expiry_date_list'

    def get_queryset(self):
        """
        Return all the products in the store
        """
        return ProductsList.objects.order_by('expiry_date')