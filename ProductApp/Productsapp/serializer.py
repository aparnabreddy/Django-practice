from rest_framework import serializer
from Productsapp.models import Product
class Productserializer(serializer.ModelSerializer):
    class Meta:
        model=Product
        fields=("name","price")