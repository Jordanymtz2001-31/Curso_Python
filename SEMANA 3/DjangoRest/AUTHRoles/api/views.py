from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAdmin, IsUser, IsAdminOrUser
from .models import Usuario
from .serializer import UsuarioSerializer

# Create your views here.
class BienvenidaView(APIView):
    permission_classes = [AllowAny] #Acceso libre
    def get(self, request):
        return Response({'mensaje': 'Bienvenido al sistema!'})

class ConfigView(APIView):
    permission_classes = [IsAdmin]
    def get(self, request):
        return Response({'mensaje': 'Configuracion del sistema (solo ADMINISTRADORES)'})
    
class InfoView(APIView):
    permission_classes = [IsUser]
    def get(self, request):
        return Response({'mensaje': 'Informacion del sistea (solo USUARIOS)'})
    
class AyudaView(APIView):
    permission_classes = [IsAdminOrUser]
    def get(self, request):
        return Response({'mensaje': 'Seccion de ayuda. (ADMIN y USER)'})
    
class RegistroView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado con exito!'})
        return Response(serializer.errors, status=400)