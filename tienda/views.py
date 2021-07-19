from django.shortcuts import render
from .models import Producto, CategoriaProductos

def tienda(request):
    productos=Producto.objects.all()
    categorias=CategoriaProductos.objects.all()
    return render(request, 'tienda/tienda.html',{'productos':productos})
