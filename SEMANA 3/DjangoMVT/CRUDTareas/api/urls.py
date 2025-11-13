from django.urls import path
from .views import listar_y_crear, update_tareas

urlpatterns = [
    path('', listar_y_crear, name='listar_tareas_url'),
    path('update/<int:tarea_id>/', update_tareas, name='update_tarea_url')
]