from rest_framework import viewsets
from .models import Carros
from .serializer import CarroSerializer

# Create your views here.
class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    serializer_class = CarroSerializer
    
""" 
VIEW SETS

Agrupan en una sola clase todos los metodos del CRUD.
Se usa un ROUTER para generar dinamicamente las URLS de las acciones logicas
Las acciones implementan los Mixin
Los Mixin son clases reutilizables que implementan un comportamiento especifico de las vistas REST

Por ejemplo:

Accion(metodo)  -  HTTP     -       URL     -       Mixin
list()              GET          /endpoint/         LisModelMixin
create()            POST         /endpoint/         CreateModelMixin
retrive()           GET          /endpoint/{id}/    RetrieveModelMixin

"""
