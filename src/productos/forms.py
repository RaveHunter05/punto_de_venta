from django.forms import ModelForm
from .models import Product, Supplier, Categorie

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