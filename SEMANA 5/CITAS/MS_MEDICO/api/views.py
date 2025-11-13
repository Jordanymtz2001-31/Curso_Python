from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Medico
from .serializer import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    # Metodo para buscar por id_cita de Medico
    @action(detail=False, methods=['get'], url_path='buscar_por_cita/(?P<id_cita>\\d+)')
    def buscar_por_cita(self, request, id_cita=None):
        medicos = Medico.objects.filter(id_cita=id_cita)
        serializer = self.get_serializer(medicos, many=True)
        return Response(serializer.data)
    
