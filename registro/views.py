from django.shortcuts import render

def register(request):
    context={}
    return render(request, 'registro/register.html', context)

def login(request):
    context={}
    return render(request, 'registro/login.html', context)

