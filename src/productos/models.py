from django.db import models

# Create your models here.
#Cambiar el nombre del modelo a inventario de productos
# 2 formularios uno de compras y uno para ventas

class Suppliers(models.Model):
    company_name = models.CharField(max_length=120)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    postal_code = models.IntegerField(null=False)
    country = models.CharField(max_length=120)
    phone = models.CharField(max_length=129)
    home_page = models.CharField(max_length= 120)

    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=False)
    picture = models.ImageField(upload_to='imagenes_productos/categories/')
    
    def __str__(self):
        return self.title

class IngresarProductos(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='imagenes_productos/products/')
    unidades_stock = models.IntegerField(null=False)
    unidades_orden = models.IntegerField(null=False)
    suppliers_id = models.ForeignKey(
        Suppliers,
        on_delete=models.CASCADE
    )
    categories_id = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Falta cantidad, categoria
    # Medida (kg, libra, quintal, etc)
    #Aqui haria falta escribir el proveedor y la categoría del producto
    #Costo se hace en las compras

    def __str__(self):
        return self.title

# En ventas:  id factura, fecha, total, id cliente
# Detalle de ventas: id producto, 
# id ventas, descuento, IVA, subtotal, cantidad

class Employees(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    titulo_cortesia = models.CharField(max_length=120)
    birthday = models.DateField()
    fecha_contrato = models.DateField()
    direccion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    codigo_postal = models.CharField(max_length=30)
    pais = models.CharField(max_length=120)
    telefono = models.CharField(max_length=120)
    extension = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='imagenes_productos/empleados/')
    notas = models.TextField()

    def __str__(self):
        return self.title

class Customers(models.Model):
    company_name = models.CharField(max_length=240)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    postal_code = models.IntegerField(null = False)
    country = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)

class Shippers(models.Model):
    company_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)

class Orders(models.Model):
    customers_id = models.ForeignKey(
        Customers,
        on_delete = models.CASCADE
    )
    employees_id = models.ForeignKey(
        Employees,
        on_delete = models.CASCADE
        #Aqui faltan los otros datos de las tablas, tengo sueño xd
    )
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField(null=False)

class Order_details(models.Model):
    orders_id = models.ForeignKey(
        Orders,
        on_delete = models.CASCADE
    )
    products_id = models.ForeignKey(
        IngresarProductos,
        on_delete = models.CASCADE
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(null = False)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    