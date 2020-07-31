from django.db import models

# Create your models here.

class Productos(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='imagenes_productos/')

    def __str__(self):
        return self.title