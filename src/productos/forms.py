from django.forms import ModelForm
from .models import Product, Supplier

class AddProducts(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AddSupplier(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'