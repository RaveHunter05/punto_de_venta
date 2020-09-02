from django.forms import ModelForm
from .models import Product, Supplier, Categorie, Employee

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