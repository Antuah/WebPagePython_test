from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm

#Metodo que devuelve una respuesta en formato JSON
def lista_productos(request):
    #Obtener todas las instancias del objeto de la BD
    productos = Producto.objects.all()

    #Construir una variable en formato de diccionario
    #Por que el JSONResponse lo necesita
    data = [
        #Objeto de producto construido al aire
        {
        'nombre': p.nombre,
        'precio': p.precio,
        'imagen': p.imagen
        }
        for p in productos
    ]

    #Devolver una respuesta en formato JSON
    return JsonResponse(data, safe=False)

#Funcion para mandar a la vista de form 
def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta de form 
    if request.method == 'POST':
        #Crear una instancia del form 
        form = ProductoForm(request.POST)

        #Validar el form 
        if form.is_valid():
            #Guardar el form en la BD
            form.save()
            return redirect('lista')
    else:
        #Crear una instancia del form 
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})