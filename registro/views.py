from django.shortcuts import redirect, render
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form=UserRegisterForm()
    context={'registerForm':form}
    return render(request, 'registro/register.html', context)
