
from django import urls
from django.contrib import admin
from django.urls import path, include
from tiendaonlineapp import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tiendaonlineapp.urls')),
    path('servicios/',include('servicios.urls')),
    path('blog/',include('blog.urls')),
    path('contacto/',include('contacto.urls')),
    path('tienda/',include('tienda.urls')),
    path('carro/',include('carro.urls')),
]

