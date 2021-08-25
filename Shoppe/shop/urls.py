from django.urls import path
from . import views
urlpatterns = [

    # API's
    path('addshop/',views.shopPage,name="shopPage"),
    path('viewall/',views.shop_list,name='shop_list'),
    path('viewshop/<id>',views.shop_details,name='shop_details'),


# views
    path('register/',views.add_shop,name="add_shop"),
    path('viewallshops/',views.view_all,name="view_all"),
    path('updateshop/',views.update_shop,name="update_shop"),
    path('contact/',views.contact_shop,name="contact_shop"),


    
]