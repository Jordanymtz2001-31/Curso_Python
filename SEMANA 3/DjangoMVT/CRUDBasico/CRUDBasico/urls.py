from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #Ruta base o PATH
    path('mascotas/', include('api.urls'))
]

""" 
mascotas/ = [
    
    listar/
    guardar/
    editar/1/
    eliminar/1/
    buscar/
    
]

"""
