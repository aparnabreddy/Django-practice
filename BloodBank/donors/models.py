from django.db import models

# Create your models here.
class donor(models.Model):
    blood_group=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    mobile=models.BigIntegerField()
    last_donated_date=models.DateField()
    

   

