from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import requests
from shop.serializer import shopSerializer
from shop.models import shop
from rest_framework.parsers import JSONParser 
from rest_framework import status



# Create your views here.
def add_shop(request):
    return render(request,'register.html')

def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/Shop/viewall/").json()

    return render(request,'viewallshops.html',{"data":fetchdata})

def update_shop(request):
    return render(request,'updateshop.html')

def contact_shop(request):
    return render(request,'contact.html')


@csrf_exempt
def shopPage(request):
    if(request.method=="POST"):
        shop_serialize=shopSerializer(data=request.POST)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shops=shop.objects.all()
        shop_serializer=shopSerializer(shops,many=True)
        return JsonResponse(shop_serializer.data,safe=False)

def shop_details(request,id):
    try:
        shops=shop.objects.get(id=id)
        if(request.method =="GET"):
            shop_serializer=shopSerializer(shops)
            return JsonResponse(shop_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            shops.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            shop_serializer=shopSerializer(shop,data=mydict)
            if(shop_serializer.is_valid()):
                shop_serializer.save()
                return JsonResponse(shop_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(shop_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except shop.DoesNotExist:
        return HttpResponse("invalid shop Id",status=status.HTTP_404_NOT_FOUND)