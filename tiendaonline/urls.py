
from django import urls
from django.contrib import admin
from django.urls import path, include
from tiendaonlineapp import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tiendaonlineapp.urls')),
    path('servicios/',include('servicios.urls')),
    path('blog/',include('blog.urls')),
    path('contacto/',include('contacto.urls')),
    path('tienda/',include('tienda.urls')),
    path('carro/',include('carro.urls')),
    path('cuenta/',include('registro.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

