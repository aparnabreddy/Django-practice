from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class sellers(models.Model):
    seller_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phone_no=models.BigIntegerField()
    DOB=models.DateField()
    district=models.CharField(max_length=50)
    age=models.IntegerField()
    aadhar_no=BigIntegerField()
