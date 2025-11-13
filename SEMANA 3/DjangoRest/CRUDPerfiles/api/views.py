from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Perfil
from .serializer import PerfilSerializer

# Create your views here.
@api_view(['GET'])
def listar_perfil(request):
    perfiles = Perfil.objects.all() #Obtenemos todos los registros de la bd
    #Serialiamos la lista de perfiles y la almacenamos en una variable "serializador"
    #many=True indica que la serializacion se tiene que aplicar a cada uno de los elementos de la coleccion de perfiles.
    serializador = PerfilSerializer(perfiles, many=True)
    return Response(serializador.data)

@api_view(['POST'])
def crear_perfil(request):
    #Deserializamos el curpo de la peticion de un objeto JSON a un objeto python y lo almacenamos en la variale "deserializador"
    deserializador = PerfilSerializer(data = request.data)
    if deserializador.is_valid(): #Si el objeto es valido
        deserializador.save() #Lo guardamos
        #Retornamos el objeto y un status 201
        return Response(deserializador.data, status=status.HTTP_201_CREATED)
    #Si no es valido entonces retornamos el error y un status 400
    return Response(deserializador.errors, status=status.HTTP_400_BAD_REQUEST)
