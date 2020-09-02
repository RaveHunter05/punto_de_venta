from django.shortcuts import render
from .models import Product

#Aqui importa todo para el form

from .forms import AddProducts, AddSupplier, AddCategorie, AddEmployee, AddCustomer

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

def add_categorie(request):
    if(request.method == 'POST'):
        form = AddCategorie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddCategorie
    
    return render(request, 'AddCategorie.html', {'form': form})

def add_employee(request):
    if(request.method == 'POST'):
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddEmployee
    
    return render(request, 'AddEmployee.html', {'form': form})

def add_customer(request):
    if(request.method == 'POST'):
        form = AddCustomer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddCustomer
    return render(request, 'AddCustomer.html', {'form': form})