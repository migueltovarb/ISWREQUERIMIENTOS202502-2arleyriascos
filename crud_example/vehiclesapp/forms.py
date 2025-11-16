from django import forms
from .models import vehiculo

#creating a form
class vehiculoForm(forms.ModelForm):

    #create meta class
    class Meta:
        #specify model to be used
        model = vehiculo

        #specify fields to be used
        fields = [
            "placa",
            "marca",
            "color_vehiculo",
            "modelo",
        ]

        fields ={
            "placa",
            "marca",
            "modelo",
            "color_vehiculo",
        }
        labels = {
            "placa": "Numero de placa",
            "marca": "Marca del vehiculo",
            "modelo": "Modelo del modelo",
            "color_vehiculo": "Color del vehiculo",
        }

        widgets = {
            "placa": forms.TextInput(attrs={'class': 'form-control'}),
            "marca": forms.TextInput(attrs={'class': 'form-control'}),
            "modelo": forms.NumberInput(attrs={'class': 'form-control'}),
            "color_vehiculo": forms.Select(attrs={'class': 'form-control'}),
        }
