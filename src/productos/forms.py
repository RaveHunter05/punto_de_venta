from django.forms import ModelForm
from .models import Productos

class NameForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'