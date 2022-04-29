from django.urls import path, register_converter
from datetime import date, datetime

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsView.as_view(), name='index'),
    path('add/', views.get_information_product, name='Add product'),
]