from django.test import TestCase
from .models import ProductsList
import datetime

# Create your tests here.

def create_product(gtin, expiry_date):
    return ProductsList.objects.create(gtin=gtin, expiry_date=expiry_date)

class ProductsListModelTest(TestCase):
    def test_create_model(self):
        product = create_product(1, '2001-01-01')
        response = self.client.get('/product/')
        self.assertQuerysetEqual(response.context['product_expiry_date_list'], [product])

    def test_create_two_products(self):
        product1 = create_product(1, '2001-01-01')
        product2 = create_product(2, '2022-04-30')
        response = self.client.get('/product/')
        self.assertQuerysetEqual(response.context['product_expiry_date_list'], [product1, product2])