from rest_framework import serializers
from shop.models import shop
class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model=shop
        fields =('shop_name','address','email','website','phone_no','username','password','confirm_password')