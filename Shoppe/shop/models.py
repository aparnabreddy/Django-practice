from django.db import models

# Create your models here.
class shop(models.Model):
    shop_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    phone_no=models.BigIntegerField(max_length=40)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

