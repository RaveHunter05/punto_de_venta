from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Supplier)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Shipper)
admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Invoice)
