from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ProductCreationForm

# Create your views here.
def brand(request):
    return HttpResponse("Creación de Brands")


def product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            #aquí se hace el ingreso a la base de datos
            return HttpResponse("Producto Creado Correctamente")
    else:
        form = ProductCreationForm()

    return render(request, 'newProduct.html', {'form': form})


def main(request):
    return render(request, 'base.html')
