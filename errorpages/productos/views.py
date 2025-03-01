from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varial al mismo tiempo
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):
    #1 Saber a que objeto hago referencia
    queryset = Producto.objects.all()
    #2 Serularizar el objeto
    serializer_class = ProductoSerializer
    #3 Renderizar la vista
    renderer_classes = [JSONRenderer] #Vamos a renderizar la vista en formato JSON
    #4 Que metodos vamos a permitir
    #http_method_names = ['get','post','put','delete'] #Permitir los metodos GET, POST, PUT y DELETE