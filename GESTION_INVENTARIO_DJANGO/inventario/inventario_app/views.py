from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, MovimientoInventario
from .forms import ProductoForm, MovimientoEntradaForm, MovimientoSalidaForm


# ----------------------------
# INICIO
# ----------------------------
def inicio(request):
    return render(request, 'index.html')

# ----------------------------
# LISTAR PRODUCTOS
# ----------------------------
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


# ----------------------------
# REGISTRAR PRODUCTO
# ----------------------------
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'registrar_producto.html', {'form': form})


# ----------------------------
# REGISTRAR ENTRADA DE PRODUCTO
# ----------------------------
def registrar_entrada(request):
    if request.method == 'POST':
        form = MovimientoEntradaForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.tipo = 'entrada'
            movimiento.save()

            # Actualizar el stock del producto
            producto = movimiento.producto
            producto.cantidad += movimiento.cantidad
            producto.save()

            return redirect('/')

    else:
        form = MovimientoEntradaForm()

    return render(request, 'registrar_entrada.html', {'form': form})

# ----------------------------
# REGISTRAR SALIDA DE PRODUCTO
# ----------------------------
def registrar_salida(request):
    if request.method == 'POST':
        form = MovimientoSalidaForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.tipo = 'salida'

            # Validar stock suficiente
            producto = movimiento.producto
            if movimiento.cantidad > producto.cantidad:
                form.add_error('cantidad', 'No hay suficiente stock disponible.')
            else:
                movimiento.save()

                producto.cantidad -= movimiento.cantidad
                producto.save()

                return redirect('/')

    else:
        form = MovimientoSalidaForm()

    return render(request, 'registrar_salida.html', {'form': form})

# ----------------------------
# ACTUALIZAR PRODUCTO
# ----------------------------
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

# ----------------------------
# ELIMINAR PRODUCTO
# ----------------------------
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'confirmar_eliminacion.html', {'producto': producto})



