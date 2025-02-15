from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categorias, name='lista'),
    path('agregar/', agregar_categoria, name='agregarC'),
    path('json/', json_categoria, name='json_categoria'),
]