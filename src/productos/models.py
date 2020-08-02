from django.db import models

# Create your models here.

class Productos(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='imagenes_productos/')
    
    #Aqui haria falta escribir el proveedor y la categoría del producto

    def __str__(self):
        return self.title