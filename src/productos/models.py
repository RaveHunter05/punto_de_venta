from django.db import models

# Create your models here.
#Cambiar el nombre del modelo a inventario de productos
# 2 formularios uno de compras y uno para ventas
class IngresarProductos(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='imagenes_productos/')
    #Falta cantidad, categoria
    # Medida (kg, libra, quintal, etc)
    #Aqui haria falta escribir el proveedor y la categoría del producto
    #Costo se hace en las compras

    def __str__(self):
        return self.title

# En ventas:  id factura, fecha, total, id cliente
# Detalle de ventas: id producto, 
# id ventas, descuento, IVA, subtotal, cantidad

