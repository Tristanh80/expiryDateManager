from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ProductsList

# Create your views here.

class ProductsView(generic.ListView):
    template_name = 'date/list.html'
    context_object_name = 'product_expiry_date_list'

    def get_queryset(self):
        """
        Return all the products in the store
        """
        return ProductsList.objects.order_by('expiry_date')

def get_information_product(request):
    if request.method == 'POST':
        gtin = request.POST.get('gtin')
        expiry_date = request.POST.get('expiry_date')
        try:
            ref = ProductsList.objects.get(gtin=gtin)
            ref.expiry_date = expiry_date
            ref.save()
            return HttpResponseRedirect('/product')
        except:
            obj = ProductsList(gtin = gtin, expiry_date=expiry_date)
            obj.save()
            return HttpResponseRedirect('/product')
    else:
        return render(request, 'date/addproduct.html')

def add_product(request, gtin, date):
    obj = ProductsList(gtin=gtin, expiry_date=date)
    obj.save()
    return HttpResponseRedirect('/product')