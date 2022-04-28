from django.urls import path, register_converter
from datetime import date, datetime

from . import views

# class DateConverter:
#     regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

#     def to_python(self, value):
#         return datetime.strptime(value, '%Y-%m-%d')

#     def to_url(self, value: date):
#         return value.strftime('%Y-%m-%d')

app_name = 'products'
# register_converter(DateConverter, 'yyyy')
urlpatterns = [
    path('', views.ProductsView.as_view(), name='index'),
    path('add/', views.addView),
    path('add/<int:gtin>/<str:date>', views.add_product, name='Add product')
]