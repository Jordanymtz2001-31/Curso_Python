from django.urls import path
from .views import *

urlpatterns = [
    path('lista/', listar_alumnos, name='listar_alumnos_url'),
    path('guardar/', guardar_alumno, name='guardar_alumno_url'),
    path('editar/<int:id>/', editar_alumno, name='editar_alumno_url'),
    path('eliminar/<int:id>/', eliminar_alumno, name='eliminar_alumno_url'),
    path('buscar/', buscar_alumnos_por_grado, name='buscar_alumnos_grado_url'),
]
