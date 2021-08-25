from product.models import product
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from product.serializer import productSerializer
from product.models import product
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def add_product(request):
    return render(request,'addproduct.html')


@csrf_exempt 
def productPage(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        product_serialize=productSerializer(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=product.objects.all()
        product_serializer=productSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)

@csrf_exempt
def product_details(request,id):
    try:
        products=product.objects.get(id=id)
        if(request.method =="GET"):
            product_serializer=productSerializer(products)
            return JsonResponse(product_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            products.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            product_serializer=productSerializer(product,data=mydict)
            if(product_serializer.is_valid()):
                product_serializer.save()
                return JsonResponse(product_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except product.DoesNotExist:
        return HttpResponse("Invalid Product Id",status=status.HTTP_404_NOT_FOUND)

