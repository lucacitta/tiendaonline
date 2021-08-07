from django.shortcuts import render
from .models import Categoria, Post


def blog(request):
    posts=Post.objects.all()
    categorias=Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts,'categorias':categorias})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    print (categoria)
    return render(request, 'blog/categorias.html', {'posts':posts,'categoria':categoria})