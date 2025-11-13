from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trabajadores, RespaldoTrabajadores
from .serializers import TrabajadorSerializer, RespaldoTrabajadorSerializer
from .services import ejecutar_respaldo

# Create your views here.
class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajadores.objects.all()
    serializer_class = TrabajadorSerializer
    
    @action(detail=False, methods=['get'])
    def respaldo(self, request):
        ejecutar_respaldo()
        return Response({'mensaje': 'Respaldo ejecutado correctamente.'})
    
class RespaldoTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = RespaldoTrabajadores.objects.all()
    serializer_class = RespaldoTrabajadorSerializer
