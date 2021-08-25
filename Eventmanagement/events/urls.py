from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.register_event,name="register_event"),
    path('addevent/',views.add_event,name="add_event"),
    path('viewallevents/',views.event_list,name='event_list'),
    path('viewevent/<fetchid>',views.event_details,name='event_details')
]