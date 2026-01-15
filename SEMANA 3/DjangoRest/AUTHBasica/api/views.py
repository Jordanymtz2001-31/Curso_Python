from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegistroSerializer

# Creamos metodos de acceso con los decoradores @api_view para API basicas, en este proyecto es mas sencillo para entender
# Con @permission_classes igual es mas sencillo en este caso
@api_view(['POST'])
@permission_classes([AllowAny]) #Registro libre, cualquiera se puede registrar
def registrar_usuario(request):
    #Serialiamos el usuario y contraseña (cuerpo de la peticion)
    serializer = RegistroSerializer(data = request.data)
    #Aqui se crea el dic automaticamente validated_data con los datos validados
    if serializer.is_valid():
        serializer.save() #Se ejecuta la funcion create automaticamente
        return Response({'mensaje': 'Usuario creado con exito!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny]) #Acceso libre
def bienvenida(request):
    return Response({'Mensaje': 'Bienvenido a la API Publica.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated]) #Acceso protegido, solo usuarios autenticados
def informacion(request):
    return Response({'info': 'Podiste Entrar con Autenticacion basica'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def noticias(request):
    return Response({'noticias': 'Noticias privadas solo para usuarios autenticados.'})