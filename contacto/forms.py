from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Textarea, Widget

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Ingresa tu nombre', max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Ingresa tu email', max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    contenido=forms.CharField(label='Ingresa tu consulta', max_length=200, required=True, widget=forms.Textarea(attrs={'class':'form-control'}))

