from .models import *
from django.forms import ModelForm

class Formulario_Compra(ModelForm):
    class Meta:
        model=Compra
        fields=['proveedor', 'metodo_pago']