from django.urls import path
from .views import *

urlpatterns = [
    path('lista', listar_instructores, name='listar_instructores_url'),
    path('guardar', guardar_instructores, name='guardar_instructores_url'),
    path('editar/<int:id>/', editar_instructor, name='editar_instructor_url'),
    path('eliminar/<int:id>/', eliminar_instructor, name='eliminar_instructor_url'),
    path('buscar', buscar_instructor, name='buscar_instructor_url'),
]