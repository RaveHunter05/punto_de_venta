from django.forms import ModelForm
from .models import IngresarProductos

class NameForm(ModelForm):
    class Meta:
        model = IngresarProductos
        fields = '__all__'