from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import CategoriaProductos, Producto

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=('updated',)

admin.site.register(CategoriaProductos)
admin.site.register(Producto, ProductosAdmin,)