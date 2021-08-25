from django.shortcuts import render
from sellers.models import sellers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from sellers.serializer import sellersSerializer
from sellers.models import sellers
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def add_seller(request):
    return render(request,'sellerdetails.html')


@csrf_exempt 
def sellersPage(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        sellers_serialize=sellersSerializer(data=mydict)
        if(sellers_serialize.is_valid()):
            sellers_serialize.save()
            return JsonResponse(sellers_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def sellers_list(request):
    if(request.method=="GET"):
        seller=sellers.objects.all()
        sellers_serializer=sellersSerializer(seller,many=True)
        return JsonResponse(sellers_serializer.data,safe=False)

@csrf_exempt
def sellers_details(request,fetchname):
    try:
        seller=sellers.objects.get(seller_name=fetchname)
        if(request.method =="GET"):
            sellers_serializer=sellersSerializer(seller)
            return JsonResponse(sellers_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            sellers.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            sellers_serializer=sellersSerializer(seller,data=mydict)
            if(sellers_serializer.is_valid()):
                sellers_serializer.save()
                return JsonResponse(sellers_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(sellers_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except sellers.DoesNotExist:
        return HttpResponse("Invalid Seller Id",status=status.HTTP_404_NOT_FOUND)
