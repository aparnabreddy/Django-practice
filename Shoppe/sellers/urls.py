from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.add_seller,name="add_seller"),
    path('addseller/',views.sellersPage,name="sellersPage"),
    path('viewall/',views.sellers_list,name="sellers_list"),
    path('viewseller/<fetchname>',views.sellers_details,name="sellers_details"),
    
]