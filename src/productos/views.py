from django.shortcuts import render
from .models import Product

#Aqui importa todo para el form

from .forms import AddProducts, AddSupplier

# Create your views here.


def productos(request):
    productos = Product.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'principal.html', context)

def add_product(request):
    if request.method == 'POST':
        form = AddProducts(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddProducts()
        
    return render(request, 'IngresarProductos.html', {'form': form})

def add_supplier(request):
    if(request.method == 'POST'):
        form = AddSupplier(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddSupplier()
    return render(request, 'AddSupplier.html', {'form': form})