from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Stock, Precio
from .forms import ProductoForm, StockForm, PrecioForm

def index(request):
    return render(request, 'index.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Redirige a la lista de productos después de agregar uno nuevo
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'lista_productos.html', {'productos': productos})

def lista_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'lista_stock.html', {'stocks': stocks})

def lista_precios(request):
    precios = Precio.objects.all()
    return render(request, 'lista_precios.html', {'precios': precios})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    stock = Stock.objects.filter(producto=producto).first()  # Para manejar casos donde no hay stock
    precio = Precio.objects.filter(producto=producto).latest('id')  # Para manejar casos donde no hay precio
    return render(request, 'detalle_producto.html', {
        'producto': producto,
        'stock': stock,
        'precio': precio
    })