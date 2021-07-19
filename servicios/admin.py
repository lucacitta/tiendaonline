from servicios.models import Servicio
from django.contrib import admin

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Servicio, ServicioAdmin)
