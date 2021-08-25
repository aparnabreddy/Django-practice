from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

from Productsapp.serializer import Productserializer

from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def product_details(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        product_serialize=Productserializer(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
