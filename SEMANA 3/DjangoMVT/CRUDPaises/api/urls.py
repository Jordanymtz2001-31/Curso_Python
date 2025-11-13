from django.urls import path
from .views import listar_paises, guardar_pais, editar_pais, eliminar_pais, buscar_pais

urlpatterns = [
    path("listar/", listar_paises, name='listar_pais_url'),
    path("guardar/", guardar_pais, name='guardar_pais_url'),
    path("editar/<int:idPais>/", editar_pais, name='editar_pais_url'),
    path("eliminar/<int:idPais>/", eliminar_pais, name='eliminar_pais_url'),
    path("buscar/", buscar_pais, name='buscar_pais_url')
]

""" 
    http://localhost:8000/paises/listar/
    http://localhost:8000/paises/guardar/
    http://localhost:8000/paises/editar/1/
    http://localhost:8000/paises/eliminar/1/
    http://localhost:8000/paises/buscar/
    
"""
