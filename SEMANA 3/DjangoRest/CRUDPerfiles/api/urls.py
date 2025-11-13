from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_perfil, name='listar_perfiles'),
    path('guardar/', views.crear_perfil, name='guardar_perfiles')
]