from rest_framework import viewsets
from .models import Empleados
from .serializer import EmpleadosSerializer

# Create your views here.
class EmpleadoViewSets(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
