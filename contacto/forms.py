from django import forms
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label='Ingresa tu nombre', max_length=100, required=True)
    email=forms.EmailField(label='Ingresa tu email', max_length=100, required=True)
    contenido=forms.CharField(label='Ingresa tu consulta', max_length=200, required=True, widget=forms.Textarea)