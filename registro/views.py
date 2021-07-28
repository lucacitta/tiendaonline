from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form=UserCreationForm()
    context={'registerForm':form}
    return render(request, 'registro/register.html', context)

def login(request):
    context={}
    return render(request, 'registro/login.html', context)

