from django.urls import path
from .views import *

urlpatterns = [
    path('lista', listar_mascotas, name='listar_mascotas_url'),
    path('guardar', guardar_mascotas, name='guardar_mascotas_url'),
    path('editar/<int:id>/', editar_mascota, name='editar_mascota_url'),
    path('eliminar/<int:id>/', eliminar_mascota, name='eliminar_mascota_url'),
    path('buscar', buscar_mascota, name='buscar_mascota_url'),
]