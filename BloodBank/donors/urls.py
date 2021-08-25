from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.add_donor,name="add_donor"),
    path('search/',views.search_donor,name="search_donor"),
    path('adddonor/',views.donorPage,name="donorPage"),
    path('viewalldonors/',views.donor_list,name="donor_list"),
    path('viewdonor/<fetchblood_group>',views.donor_details,name="donor_details"),

]