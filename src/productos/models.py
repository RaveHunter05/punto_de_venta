from django.db import models

# Create your models here.
#Cambiar el nombre del modelo a inventario de productos
# 2 formularios uno de compras y uno para ventas

class Supplier(models.Model):
    company_name = models.CharField(max_length=120, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=120, null=False)
    region = models.CharField(max_length=120, null=False)
    postal_code = models.IntegerField(null=False)
    country = models.CharField(max_length=120, null=False)
    phone = models.CharField(max_length=129, null=False)
    home_page = models.CharField(max_length= 120)

    def __str__(self):
        return self.title

class Categorie(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    picture = models.ImageField(upload_to='imagenes_productos/categories/', null=False)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    photo = models.ImageField(upload_to='imagenes_productos/products/', null=False)
    unidades_stock = models.IntegerField(null=False)
    unidades_orden = models.IntegerField(null=False)
    suppliers_id = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=False
    )
    categories_id = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        null=False
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

class Employee(models.Model):
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    title = models.CharField(max_length=120, null=False)
    titulo_cortesia = models.CharField(max_length=120)
    birthday = models.DateField(null=False)
    fecha_contrato = models.DateField(null=False)
    direccion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    codigo_postal = models.CharField(max_length=30)
    pais = models.CharField(max_length=120)
    telefono = models.CharField(max_length=120, null=False)
    extension = models.CharField(max_length=10, null=False)
    photo = models.ImageField(upload_to='imagenes_productos/empleados/', null=False)
    notas = models.TextField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=240, null=False)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Shipper(models.Model):
    name = models.CharField(max_length=120, null=False)
    phone = models.CharField(max_length=40)
    company_name = models.CharField(max_length=120, null=False)
    phone = models.CharField(max_length=20, null=False)
    photo = models.ImageField(upload_to='imagenes_productos/empleados/', null=False)

    def __str__(self):
        return self.title

class Order(models.Model):
    customers_id = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE,
        null=False
    )
    employees_id = models.ForeignKey(
        Employee,
        on_delete = models.CASCADE,
        null=False
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Invoice(models.Model):
    order_id = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        null=False
    )
    customers_id = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE,
        null=False
    )
    employees_id = models.ForeignKey(
        Employee,
        on_delete = models.CASCADE,
        null=False
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Order_detail(models.Model):
    orders_id = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        null=False
    )
    products_id = models.ForeignKey(
        Product,
        on_delete = models.CASCADE,
        null=False
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(null = False)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    