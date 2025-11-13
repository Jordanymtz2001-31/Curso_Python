from django.urls import path
from .views import listar_mascotas, guardar_mascota, editar_mascota, eliminar_mascota, buscar_mascota

urlpatterns = [
    path("listar/", listar_mascotas, name="listar_mascotas_url"),
    path("guardar/", guardar_mascota, name = "guardar_mascota_url"),
    path("editar/<int:idMascota>/", editar_mascota, name= "editar_mascota_url"),
    path("eliminar/<int:idMascota>/", eliminar_mascota, name = "eliminar_mascota_url"),
    path("buscar/", buscar_mascota, name="buscar_mascota_url")
]

""" 
    URL: protocolo://host:puerto/Path/endpoint
    
    URL: http://localhost:8000/mascota/listar/ <-- listar_mascotas_url
    
    GET -- Acceso, lectura
    POST -- Escritura
"""