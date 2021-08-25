
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Shop/', include('shop.urls')),
    path('Product/', include('product.urls')),
    path('Seller/', include('sellers.urls')),

]

