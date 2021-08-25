from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=50)
    product_details=models.CharField(max_length=50)
    seller_name=models.CharField(max_length=50)
    manufacture_name=models.CharField(max_length=50)
    manufactured_date=models.DateField()
    expiry_date=models.DateField()
    price=models.IntegerField()
