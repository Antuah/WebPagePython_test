from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import CategoriaForm

def lista_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
        'nombre': c.nombre,
        'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'agregarC.html', {'form': form})

# Haz una lista con el json de las categorias con 
def json_categoria(request):
 
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'listas.html', {'form': form})