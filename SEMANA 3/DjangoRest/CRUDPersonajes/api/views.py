from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Personaje
from .serializer import PersonajeSerializer
from django.shortcuts import get_object_or_404

# VISTAS BASADA EN CLASES - (CBV)
class personajesAPIView(APIView): #Listar y Guardar
    #Metodo POST para crear un nuevo personaje
    def post(self, request):
        try:
            serializer = PersonajeSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Mensaje': 'Personaje creado con exito!'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Mensaje': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    #Metodo GET para listar los personajes
    def get(self, request):
        try:
            #Recuperamos UNICAMENTE los personajes ACTIVOS
            lista_personajes = Personaje.objects.filter(activo = True)
            serializer = PersonajeSerializer(lista_personajes, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Mensaje': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class personajesBusquedaAPIView(APIView):
    #Funcion GET para buscar un personaje por nombre
    def get(self, request, nombre):
        try:
            #Busca el personaje con el mismo nombre y el campo activo verdadero
            personaje = Personaje.objects.get(nombre = nombre, activo = True)
            serializer = PersonajeSerializer(personaje)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Personaje.DoesNotExist:
            return Response({'Mensaje': 'No se encontro el personaje con ese nombre'}, status=status.HTTP_404_NOT_FOUND)
        
class personajesDetailAPIView(APIView):
    #Funcion PATCH para editar un personaje
    def patch(self, request, id):
        #Buscamos un personaje activo que coincida con la pk
        personaje = get_object_or_404(Personaje, pk = id, activo = True)
        #Serializamos el personaje indicando que sera parcial
        serializer = PersonajeSerializer(personaje, data = request.data, partial = True)
        if serializer.is_valid(): #Validamos
            serializer.save() #Guardamos
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Mensaje': 'Ingresa correctamente los datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Funcion DELETE para eliminar un personaje
    def delete(self, request, id):
        #Buscamos el personaje activo
        personaje = get_object_or_404(Personaje, pk = id, activo = True)
        #Desactivamos el personahe
        personaje.activo = False
        personaje.save()
        return Response({'Mensaje': 'Eliminado con exito!'}, status= status.HTTP_204_NO_CONTENT)
    