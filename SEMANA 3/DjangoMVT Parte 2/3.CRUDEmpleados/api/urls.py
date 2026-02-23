from django.urls import path
from .views import *


urlpatterns = [
    path('lista/', listar_empleados, name='listar_empleados_url'),
    path('guardar/', guardar_empleados, name='guardar_empleados_url'),
    path('editar/<int:id>/', editar_empleado, name='editar_empleado_url'),
    path('eliminar/<int:id>/', eliminar_empleado, name='eliminar_empleado_url'),
    path('buscar/', buscar_empleado, name='buscar_empleado_url'),
]
