from django.forms import ModelForm
from .models import Product

class NameForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'