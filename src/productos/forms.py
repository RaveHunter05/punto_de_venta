from django.forms import ModelForm
from .models import Product, Supplier, Categorie, Employee, Customer, Shipper, Order

class AddProducts(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AddSupplier(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class AddCategorie(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class AddEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AddCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AddShipper(ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'

class AddOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'