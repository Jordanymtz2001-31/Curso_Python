from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Curso, Estudiante
from .serializers import CursoSerializer, EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.filter()
    serializer_class = CursoSerializer


    #Metodo personalizado para devolver los cursos activos que no aya alcanzado el maximo cupo
    @action(detail=False, methods=['get'])
    def cursos_activos(self, request):
        cursos = Curso.objects.filter(activo=True)
        serializer = CursoSerializer(cursos, many=True) #Ahora en una variable alamcenamos la lista de cursos pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
        return Response(serializer.data)


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    #Metodo para devolver estudiantes con un promedio de mayo o igual a 9.0
    @action(detail=False, methods=['get'])
    def estudiantes_aprobados(self, request):
        estudiantes = Estudiante.objects.filter(promedio__gte=9.0)
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)