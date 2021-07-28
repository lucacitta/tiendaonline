from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

#admin.site.register(UsuariosAdmin)
