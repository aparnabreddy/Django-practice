from events.models import event
from events.serializer import eventSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.

def register_event(request):
    return render(request,'registerevent.html')


@csrf_exempt
def add_event(request):
    if(request.method=="POST"):
        eventdict=JSONParser().parse(request)
        event_serializer=eventSerializer(data=eventdict)
        if(event_serializer.is_valid()):
            event_serializer.save()
            return JsonResponse(event_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def event_list(request):
    if(request.method=="GET"):
        events=event.objects.all()
        event_serializer=eventSerializer(events,many=True)
        return JsonResponse(event_serializer.data,safe=False)

@csrf_exempt
def event_details(request,fetchid):
    try:
        events=event.objects.get(id=fetchid)
        if(request.method=="GET"):
            event_serializer=eventSerializer(events)
            return JsonResponse(event_serializer.data,status=status.HTTP_200_OK)
        
        if(request.method=="DELETE"):
            events.delete()
            return HttpResponse("Event deleted",status=status.HTTP_200_OK)

        if(request.method=="PUT"):
            eventdict=JSONParser().parse(request)
            event_serializer=eventSerializer(events,data=eventdict)
            if(event_serializer.is_valid()):
                event_serializer.save()
                return JsonResponse(event_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(event_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except event.DoesNotExist:
        return HttpResponse("Invalid event title",status=status.HTTP_404_NOT_FOUND)



        