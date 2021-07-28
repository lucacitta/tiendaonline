from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        username=request.POST.get('username')
        messages.success(request,f'Usuario {username} creado')
    else:
        form=UserCreationForm()
    context={'registerForm':form}
    return render(request, 'registro/register.html', context)

def login(request):
    context={}
    return render(request, 'registro/login.html', context)

