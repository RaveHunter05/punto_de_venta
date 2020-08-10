from django.shortcuts import render
from .models import IngresarProductos

#Aqui importa todo para el form

from .forms import NameForm

# Create your views here.


def productos(request):
    productos = IngresarProductos.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'principal.html', context)

def ingresar_productos(request):
    if request.method == 'POST':
        form = NameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NameForm()
        
    return render(request, 'IngresarProductos.html', {'form': form})