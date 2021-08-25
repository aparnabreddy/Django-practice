from rest_framework import serializers
from donors.models import donor
class donorSerializer(serializers.ModelSerializer):
    class Meta:
        model=donor
        fields =('blood_group','name','address','pincode','mobile','last_donated_date')