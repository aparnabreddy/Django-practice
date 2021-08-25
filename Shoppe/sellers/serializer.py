from rest_framework import serializers
from sellers.models import sellers
class sellersSerializer(serializers.ModelSerializer):
    class Meta:
        model=sellers
        fields =('seller_name','address','email','phone_no','DOB','district','age','aadhar_no')