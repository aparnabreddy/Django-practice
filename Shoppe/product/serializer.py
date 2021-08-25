from rest_framework import serializers
from product.models import product
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields =('product_name','product_details','seller_name','manufacture_name','manufactured_date','expiry_date','price')