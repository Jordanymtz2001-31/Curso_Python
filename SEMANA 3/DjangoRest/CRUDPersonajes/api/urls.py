from django.urls import path
from .views import personajesAPIView, personajesBusquedaAPIView, personajesDetailAPIView

urlpatterns = [
    path('', personajesAPIView.as_view(), name='personaje'), #Listar y Guardar
    path('detail/<int:id>/', personajesDetailAPIView.as_view(), name='detail'), #Editar y Eliminar
    path('busqueda/<str:nombre>/', personajesBusquedaAPIView.as_view(), name='busqueda')
]