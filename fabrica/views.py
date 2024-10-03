# fabrica/views.py
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'fabrica/listar_productos.html', {'productos': productos})

def fabrica_view(request):
    productos = Producto.objects.all()
    return render(request, 'fabrica/fabrica.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fabrica/')
    else:
        form = ProductoForm()
    return render(request, 'fabrica/agregar_producto.html', {'form': form})