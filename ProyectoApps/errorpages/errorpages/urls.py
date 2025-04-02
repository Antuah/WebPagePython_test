from django.contrib import admin
from django.urls import path, include
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('error/', error, name='error'),
    path('onepage/', onepage, name='onepage'),
    path('prueba/', prueba, name='prueba'),
    path('search/', search_view, name='search'),
    path('error_logs/', error_logs, name='error_logs'),
    path('api/error_logs/', get_error_logs, name='get_error_logs'),
    path('users/', include('users.urls')),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('alumnos/', include('alumnos.urls')),
]
