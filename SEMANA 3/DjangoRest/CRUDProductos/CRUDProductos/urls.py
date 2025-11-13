from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('api.urls'))
]

""" 
RUTAS DEL PROYECTO

http://localhost:8000/producto/         -- GET      -- listar productos
http://localhost:8000/producto/         -- POST     -- guardar productos
http://localhost:8000/producto/id/       -- PUT      -- editar productos
http://localhost:8000/producto/id/       -- GET      -- buscar productos
http://localhost:8000/producto/id/       -- DELETE   -- eliminar productos

"""
