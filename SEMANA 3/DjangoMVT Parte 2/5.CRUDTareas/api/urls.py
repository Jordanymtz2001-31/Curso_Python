from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_y_crear, name='listar_tareas_url'),
    path('editar/<int:id>/', editar_tarea, name='editar_tarea_url'),
]
