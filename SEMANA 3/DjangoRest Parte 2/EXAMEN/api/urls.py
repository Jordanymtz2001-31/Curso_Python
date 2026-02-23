from django.urls import path
from api.views import *

urlpatterns = [
    path('listar_denominaciones/', listar_denominaciones, name='listar_denominaciones'),
    path('inicializar_cajero/', incializar_cajero, name='incializar_cajero'),
    path('retirar_dinero/', retirar_dinero, name='retirar_dinero'),
    path('depositar_dinero/', depositar_dinero, name='depositar_dinero'),
]
