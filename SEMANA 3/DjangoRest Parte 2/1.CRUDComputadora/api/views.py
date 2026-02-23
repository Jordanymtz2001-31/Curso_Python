from django.shortcuts import render #Aqui ya no vamso ocupar render por que ahi ya sera una arquitectura REST
from rest_framework import status
from rest_framework.response import Response #Con Response indicamos que vamos a devolver una respuesta HTTP
from rest_framework.decorators import api_view
from api.models import Computadora
from api.serializers import CompuSerializer

# Creamos la vista
@api_view(['GET']) #Indicamos que vamos a utilizar los metodos GET con el decorador
def api_listar_computadoras(request):
    computadoras = Computadora.objects.all() #Obtenemos todas las computadoras y la asignamos a la variable
    serializer = CompuSerializer(computadoras, many=True) #Ahora en una variable alamcenamos la lista de computadoras pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
    
    #Retornamos a nuestro cliente o framework de fronted el listado de computadoras pero ya serializadas (fromaro de mensajeria JSON)
    return Response(serializer.data) #El data significa los datos que se mandaran
    
@api_view(['POST']) #Indicamos que vamos a utilizar los metodos POST con el decorador para crear una computadora
def api_guardar_computadora(request):
    deserializer = CompuSerializer(data=request.data) #Declaramos una variables para almacenar el objeto que nos manda el cliente o framework de frontend
    if deserializer.is_valid(): #Si el objeto es valido
        deserializer.save() #Guardamos el objeto
        return Response(deserializer.data, status=status.HTTP_201_CREATED) #Retornamos el objeto serializado y el estatus de creado
    
    #Si los datos no son validos
    return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)