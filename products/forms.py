from django import forms

class ProductCreationForm(forms.Form):
    title = forms.CharField(label='Nombre del Producto',max_length=20)
    summary = forms.CharField(label='Resumen del Producto', max_length=50)