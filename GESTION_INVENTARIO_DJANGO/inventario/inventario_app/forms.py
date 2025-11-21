from django import forms
from .models import Producto, MovimientoInventario

# Formulario para productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'categoria', 'cantidad', 'precio']


# Formulario para ENTRADAS de inventario
class MovimientoEntradaForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'cantidad', 'observacion']

    # asigna automáticamente el tipo "entrada"
    def save(self, commit=True):
        movimiento = super().save(commit=False)
        movimiento.tipo = 'entrada'
        if commit:
            movimiento.save()
        return movimiento


# Formulario para SALIDAS de inventario
class MovimientoSalidaForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'cantidad', 'observacion']

    # asigna automáticamente el tipo "salida"
    def save(self, commit=True):
        movimiento = super().save(commit=False)
        movimiento.tipo = 'salida'
        if commit:
            movimiento.save()
        return movimiento