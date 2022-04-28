from django.db import models
# Create your models here.

# Define the products model
class ProductsList(models.Model):
    gtin = models.IntegerField()
    expiry_date = models.DateField()
    def __str__(self):
        return str(self.gtin)
