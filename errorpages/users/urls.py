from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *
from django.urls import include

router = SimpleRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path ('', include(router.urls)),
    #Este es el path para iniciar sesión 
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]