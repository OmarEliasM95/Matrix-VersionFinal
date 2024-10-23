from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from Productos.models import *
from Proveedores.models import *
from Empleados.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def panel_compras(request):
    id_proveedor=request.session.get('id_proveedor', None)
    if not Compra.objects.exists():
         request.session.pop('id_compra', None)
    id_compra=request.session.get('id_compra', None)

    if id_proveedor:
        proveedor=Proveedor.objects.get(id=id_proveedor)
        formulario_compra=Formulario_Compra({'proveedor':id_proveedor})
        if formulario_compra.is_valid():
            lista_productos_proveedor=Producto_Intermedia.objects.filter(proveedor=proveedor)
            contexto=({'formulario_compra':formulario_compra, 'lista_productos_proveedor':lista_productos_proveedor})
  
    else:
        formulario_compra=Formulario_Compra()
        contexto=({'formulario_compra':formulario_compra})

    if id_compra:
        compra=Compra.objects.get(id=id_compra)  
        lista_compra=compra.compra_intermedio_set.all()
        if lista_compra:
            total_compra=sum(producto.precio_de_compra for producto in lista_compra)
            compra.total=total_compra
            compra.save()
            contexto.update({'compra':compra, 'lista_compra':lista_compra})
        else: 
            compra.delete()
         

    return render(request, 'compras.html', contexto)

def seleccionar_proveedor(request):
    if request.method=='POST':
        proveedor_seleccionado=Formulario_Compra(request.POST)
        if proveedor_seleccionado.is_valid():
            id_proveedor= proveedor_seleccionado.instance.proveedor.id
            request.session['id_proveedor']=id_proveedor
            id_compra=request.session.get('id_compra', None)
            if id_compra:
                try:
                    compra=Compra.objects.get(id=id_compra)
                    compra.proveedor=proveedor_seleccionado.instance.proveedor
                    compra.save()
                except:
                    compra=Compra(id=id_compra, proveedor=proveedor_seleccionado.instance.proveedor)
                    compra.save()
            return redirect('panel_compras')
   
            

def agregar_producto_compra(request, id_producto):
    producto=Producto.objects.get(id=id_producto)
    id_compra=request.session.get('id_compra', None)

    if id_compra:
        try:
            compra=Compra.objects.get(id=id_compra)
        except:
            compra=Compra(id=id_compra)
            proveedor=Proveedor.objects.get(id=request.session.get('id_proveedor'))
            compra.proveedor=proveedor
            compra.save()
    else:
        compra=Compra()
        id_proveedor=request.session.get('id_proveedor', None)
        proveedor=Proveedor.objects.get(id=id_proveedor)
        compra.proveedor=proveedor
        compra.id=id_compra
        compra.save()
        request.session['id_compra']=compra.id

    compra.productos.add(producto)
  
    if request.method=='POST':
        precio_compra=int(request.POST.get('precio_compra'))
        cantidad=int(request.POST.get('cantidad'))
        producto_a_comprar=compra.compra_intermedio_set.get(producto=producto)
        producto_a_comprar.cantidad=cantidad
        producto_a_comprar.precio_de_compra=precio_compra
        producto_a_comprar.save()
    return redirect('panel_compras')


def eliminar_producto_compra(request, id_producto):
    id_compra=request.session.get('id_compra')
    producto_compra_a_eliminar=Compra_intermedio.objects.get(compra_id=id_compra, producto_id=id_producto)
    producto_compra_a_eliminar.delete()
    return redirect('panel_compras')

def confirmar_compra(request):
    if request.method=='POST':
        id_compra=request.session.get('id_compra')
        compra=Compra.objects.get(id=id_compra)
        formulario_compra=Formulario_Compra(request.POST)
        if formulario_compra.is_valid():
            metodo_pago=formulario_compra.cleaned_data['metodo_pago']
            compra.metodo_pago=metodo_pago
            compra.empleado=Empleado.objects.get(username=request.user.username)
            compra.id_sesion=request.session.session_key
            compra.save()
            request.session.pop('id_compra')
            request.session.pop('id_proveedor')
        lista_productos_comprados=compra.compra_intermedio_set.all()
        for producto_comprado in lista_productos_comprados:
            producto=Producto.objects.get(id=producto_comprado.producto.id)
            producto.existencias+=producto_comprado.cantidad
            producto.save()
        return redirect('panel_compras' )