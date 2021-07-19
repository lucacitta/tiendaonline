from contacto.forms import FormularioContacto
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage



def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            email=send_mail(
            f'El usuario {nombre} con email {email} envió el siguiente mensaje:',
            contenido,
            'lucacitta@gmail.com',
            ['lucacitta@gmail.com'],
            fail_silently=False,
            )
            return redirect('/contacto/?valido')
    return render(request, 'contacto/contacto.html', {'miformulario':formulario_contacto})