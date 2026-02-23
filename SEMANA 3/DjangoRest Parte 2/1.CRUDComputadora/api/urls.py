from django.urls import path

from api.views import *

urlpatterns = [
    path('listar/', api_listar_computadoras, name='api_listar_computadoras'),
    path('guardar/', api_guardar_computadora, name='api_guardar_computadora'),
]
