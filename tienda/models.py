from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from tiendaonline.settings import BASE_DIR


class CategoriaProductos(models.Model):
    nombre=models.CharField(max_length=50)

    class Meta:
        verbose_name='Categoria Producto'
        verbose_name_plural='Categorias Productos'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    precio=models.IntegerField()
    categoria=models.ForeignKey(CategoriaProductos, on_delete=CASCADE)
    imagen=models.ImageField(upload_to='BASE_DIR/staticfiles/tienda/img')
    updated=models.DateTimeField(auto_now_add=True)
    disponibilidad=models.BooleanField()


    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return self.nombre

