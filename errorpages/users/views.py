from .models import CustomUser
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#Clase que hace las vistas get/put/post/delete
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = CustomUserSerializer

    #Variables nuevas para la autenticacion
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #Sobre escribir el metodo get_permissions
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer