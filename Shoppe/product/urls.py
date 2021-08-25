from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.add_product,name="add_product"),
    path('addproduct/',views.productPage,name="productPage"),
    path('viewall/',views.product_list,name='product_list'),
    path('viewproduct/<id>',views.product_details,name='product_details'),

    
]