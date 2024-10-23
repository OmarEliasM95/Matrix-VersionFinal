from django.shortcuts import render, redirect
from Productos.models import *
from Empleados.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
@login_required
def panel_venta(request):
    lista_producto=Producto.objects.all()
    if not Venta.objects.exists():
        venta=Venta.objects.create()
        request.session['id_venta']=venta.id
        productos=venta.productos_vendidos_set.all()
        venta.total_venta=0
        for producto in productos:
            venta.total_venta+=producto.subtotal
        formularioP=Formulario_Pago()
        venta.save()
    else:
        venta=Venta.objects.last()
        request.session['id_venta']=venta.id
        productos=venta.productos_vendidos_set.all()
        venta.total_venta=0
        for producto in productos:
            venta.total_venta+=producto.subtotal
        formularioP=Formulario_Pago()
        venta.save()
    return render(request,'ventas.html', {'lista_producto':lista_producto, 'venta':venta,
                                         'productos':productos, 'formularioP':formularioP})
def agregar_producto(request,id_producto):
    id_venta=request.session.get('id_venta')
    venta=Venta.objects.get(id=id_venta)
    if request.method == 'POST':
        prod_vendidos=Producto.objects.get(id=id_producto)
        cantidad=int(request.POST.get('cantidad'))
        if Productos_Vendidos.objects.filter(venta=venta, producto=prod_vendidos).exists():
            new_producto=Productos_Vendidos.objects.get(venta=venta, producto=prod_vendidos)
            new_producto.cantidad+=cantidad
            new_producto.subtotal=new_producto.cantidad*prod_vendidos.precio
            new_producto.save()
        else:
            subtotal=prod_vendidos.precio*cantidad
            venta.productos.add(prod_vendidos,through_defaults={'cantidad':cantidad,'subtotal':subtotal})
        prod_vendidos.existencias-=cantidad
        prod_vendidos.save()
    return redirect('panel_venta')

def eliminar_producto_vendido(request, id_producto):
    id_venta=request.session.get('id_venta')
    venta=Venta.objects.get(id=id_venta)
    producto_a_eliminar=Producto.objects.get(id=id_producto)
    cantidad_eliminada=venta.productos_vendidos_set.get(producto=producto_a_eliminar).cantidad
    venta.productos.remove(producto_a_eliminar)
    producto_a_eliminar.existencias+=cantidad_eliminada
    producto_a_eliminar.save()
    return redirect('panel_venta')

def crear_factura(request, id_venta):
    venta=Venta.objects.get(id=id_venta)
    if request.method == 'POST':
        formularioP=Formulario_Pago(request.POST, instance=venta)
        if formularioP.is_valid():
            formularioP.save()
    venta.fecha=datetime.now()
    venta.empleado=Empleado.objects.get(username=request.user.username)
    venta.id_sesion=request.session.session_key
    venta.save()
    productos_a_vender=venta.productos_vendidos_set.all()
    return render(request,'factura.html',{'venta':venta,'productos_a_vender':productos_a_vender})
def nueva_venta(request):
    venta=Venta.objects.create()
    return redirect('panel_venta')