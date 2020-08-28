from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Suppliers)
admin.site.register(Categories)
admin.site.register(IngresarProductos)
admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Shippers)
admin.site.register(Orders)
admin.site.register(Order_details)
