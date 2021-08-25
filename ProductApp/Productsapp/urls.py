from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.product_details,name='product_details')
]