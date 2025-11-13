from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Postres
from .serializers import PostresSerializers
from .services import ejecutar_proc_postres

# Create your views here.
class PostresViewSets(viewsets.ModelViewSet):
    queryset = Postres.objects.all()
    serializer_class = PostresSerializers
    
    @action(detail=False, methods=['post'])
    def ejecutar_procedimiento(self, request):
        data = request.data 
        id_postre = data.get('id_postre')
        tipo = data.get('tipo')
        precio = data.get('precio')
        evento = data.get('evento')
        
        mensaje = ejecutar_proc_postres(id_postre, tipo, precio, evento)
        return Response({'mensaje': mensaje})
