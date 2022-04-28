import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Define product model
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    expiry_date = models.DateTimeField('expiry date')
    def __str__(self):
        return self.product_name