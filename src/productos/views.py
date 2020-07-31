from django.shortcuts import render
from .models import Productos
# Create your views here.


def productos():
    productos = Productos.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'principal.html', context)