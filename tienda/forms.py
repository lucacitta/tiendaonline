from django import forms
from django.forms.widgets import Textarea

class FormularioVenta(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()