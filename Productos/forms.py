from .models import *
from django import forms
from django.forms import ModelForm

class formulario_producto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    #def __init__(self):
        #super(formulario_producto, self).__init__()
        #for field in self.fields.values():
          #  field.widget.attrs.update({
         #       'class': 'input-estilo' 
           # })
