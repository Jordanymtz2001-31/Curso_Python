from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets
from .models import Departamento, Empleado
from .serializer import DepartamentoSerializer, EmpleadoSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin

class DepartamentoViewSets(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAuthenticated, IsAdmin] # Indicamos que Departamento solo puede ser accedido por un usuario autenticado y si es admin


class EmpleadoViewSets(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated] # Indicamos que Empleado solo puede ser accedido por un usuario autenticado

    #Creamos un metodo
    def get_queryset(self):
        empleado = self.request.user.empleado
        if empleado.rol == 'admin': # Si el empleado es admin, entonces retornamos todos los empleados
            return Empleado.objects.all()
        elif empleado.rol == 'gerente': # Si el empleado es gerente, entonces retornamos todos los empleados del departamento
            return Empleado.objects.filter(departamento=empleado.departamento)
        # Si el empleado es empleado, entonces retornamos todos los empleados del departamento
        return Empleado.objects.filter(departamento=empleado.id)
    
    @action(detail=False, methods=['get']) #Creamos una accion que sera una peticion GET
    def mi_perfil(self, request):
        empleado = self.request.user.empleado
        serializer = self.get_serializer(empleado)
        return Response(serializer.data)
