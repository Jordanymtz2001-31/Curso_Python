from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Paciente
from .serializer import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    # Metodo para buscar por id_cita de un paciente
    @action(detail=False, methods=['get'], url_path='buscar_por_cita/(?P<id_cita>\\d+)')
    def buscar_por_cita(self, request, id_cita=None):
        pacientes = Paciente.objects.filter(id_cita=id_cita)
        serializer = self.get_serializer(pacientes, many=True)
        return Response(serializer.data)
    