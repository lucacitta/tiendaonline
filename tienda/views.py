from carro.views import limpiar_carro
from django.shortcuts import render, redirect
from .models import Producto, CategoriaProductos
from .forms import FormularioVenta
from django.core.mail import send_mail
from tiendaonline.settings import EMAIL_HOST_USER

def tienda(request):
    productos=Producto.objects.all()
    return render(request, 'tienda/tienda.html',{'productos':productos})



def confirmacionPedido(request):
    form_venta=FormularioVenta()
    if request.method=='POST':
        form_venta=FormularioVenta(data=request.POST)
        if form_venta.is_valid():
            pedido=''
            total=0
            for key, value in request.session['carro'].items():
                pedido+=f'\nProducto: {value.get("nombre")}, cantidad: {value.get("cantidad")}, subtotal: {value.get("cantidad")*value.get("precio")}'
                total+=int(value.get("cantidad"))*int(value.get("precio"))
            pedido+=f'\nTotal del pedido: {total}'
            print(pedido)
            nombre=request.POST.get('nombre')
            apellido=request.POST.get('apellido')
            direccion=request.POST.get('direccion')
            telefono=request.POST.get('telefono')
            email=request.user.email
            subject='Confirmacion de pedido en "Tu Dulcería Favorita"'
            mensaje=f'Gracias {nombre} {apellido}\nTu pedido fue realizado con exito, nuestro equipo se pondra en contacto a la brevedad para realizar el envio a {direccion}\nInformacion del pedido\n{pedido}\nMuchas gracias por elegirnos, Tu Dulceria Favorita'

            #Email para el cliente
            send_mail(
            subject,
            mensaje,
            EMAIL_HOST_USER,
            [email,],
            fail_silently=False,)

            #Email para el administrador
            mensaje=(f'El pedido debera entregarse en {direccion},\nPor cualquier consulta el numero de telefono del cliente es {telefono}\nInformacion del pedido\n{pedido}')
            send_mail(
            f'Tienes un nuevo pedido de {nombre} {apellido}.',
            mensaje,
            EMAIL_HOST_USER,
            ['lucacitta@gmail.com'],
            fail_silently=False,)

            limpiar_carro(request, lugar='confirmacion')
            return redirect('/tienda/confirmacionPedido/?valido')
    return render(request,'tienda/confirmacion.html',{'form_venta':form_venta})
