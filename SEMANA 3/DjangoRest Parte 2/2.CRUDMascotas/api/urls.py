from django.urls import path
from api.views import *

urlpatterns = [
    path('listar_guardar/', listar_guardar_mascotas, name='listar_guardar_mascotas'),
    path('detalle/<int:id_mascota>/', detalles_mascotas, name='detalles_mascotas'),
]
