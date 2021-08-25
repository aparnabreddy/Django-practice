from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from donors.serializer import donorSerializer
from donors.models import donor
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def add_donor(request):
    return render(request,'registerdonor.html')

def search_donor(request):
    return render(request,'searchdonor.html')

@csrf_exempt 
def donorPage(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        donor_serialize=donorSerializer(data=mydict)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def donor_list(request):
    if(request.method=="GET"):
        donors=donor.objects.all()
        donor_serializer=donorSerializer(donors,many=True)
        return JsonResponse(donor_serializer.data,safe=False)

@csrf_exempt
def donor_details(request,fetchblood_group):
    try:
        donors=donor.objects.get(blood_group=fetchblood_group)
        if(request.method =="GET"):
            donor_serializer=donorSerializer(donors)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            donors.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            donor_serializer=donorSerializer(donors,data=mydict)
            if(donor_serializer.is_valid()):
                donor_serializer.save()
                return JsonResponse(donor_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(donor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except donor.DoesNotExist:
        return HttpResponse("invalid blood group",status=status.HTTP_404_NOT_FOUND)
