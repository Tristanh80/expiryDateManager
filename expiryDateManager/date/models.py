import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Define the products model
class ProductsList(models.Model):
    gtin = models.IntegerField()
    expiry_date = models.DateTimeField('expiry date')
    def __str__(self):
        return str(self.gtin)
