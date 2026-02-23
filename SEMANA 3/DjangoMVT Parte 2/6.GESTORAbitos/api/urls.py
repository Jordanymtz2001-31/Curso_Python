from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_y_crear, name='listar_habitos_url'),
    path('editar_estado/<int:id>/', editar_estado_habito, name='editar_estado_habito_url'),
    path('editar/<int:id>/', editar_habito, name='editar_habito_url'),
    path('eliminar/<int:id>/', eliminar_habito, name='eliminar_habito_url'),
]
