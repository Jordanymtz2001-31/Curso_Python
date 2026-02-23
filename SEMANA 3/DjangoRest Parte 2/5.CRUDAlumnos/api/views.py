from django.shortcuts import render
from rest_framework import viewsets
from api.models import Alumno
from api.serializers import AlumnosSerializer

class AlumnoViewSet(viewsets.ModelViewSet): #Creamos una clase que hereda de ModelViewSet, para crear todos los metodos CRUD basico
    queryset = Alumno.objects.all() #Indicamos que queremos obtener todos los alumnos
    serializer_class = AlumnosSerializer #Indicamos que queremos serializar los alumnos