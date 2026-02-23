
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Mascota
from api.serializers import MascotasSerializer


@api_view(['GET', 'POST']) #Indicamos que vamos a utilizar los metodos GET con el decorador
def listar_guardar_mascotas(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all() #Obtenemos todas las mascotas y la asignamos a la variable
        serializer = MascotasSerializer(mascotas, many=True) #Ahora en una variable alamcenamos la lista de mascotas pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
        
        #Retornamos a nuestro cliente o framework de fronted el listado de mascotas pero ya serializadas (fromaro de mensajeria JSON)
        return Response(serializer.data) #El data significa los datos que se mandaran
    
    #Pero si la peticion es POST
    elif request.method == 'POST':
        deserializer = MascotasSerializer(data=request.data) #Declaramos una variables para almacenar el objeto que nos manda el cliente o framework de frontend
        if deserializer.is_valid(): #Si el objeto es valido
            deserializer.save() #Guardamos el objeto
            return Response(deserializer.data, status=status.HTTP_201_CREATED) #Retornamos el objeto serializado y el estatus de creado
        
        #Si los datos no son validos
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Si no se cumple ninguna de las condiciones anteriores
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) 
def detalles_mascotas(request, id_mascota):
    try:
        mascota = Mascota.objects.get(id=id_mascota)#Primero buscamos la mascota en la base de datos
        #Pero si no existe la mascota respondemos con un 404 Not Found que indica que no se ha encontrado
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #Si la peticion es GET
        serializer = MascotasSerializer(mascota) #Ahora en una variable alamcenamos la mascota pero ya serializada, (UN SOLO OBJETO)
        return Response(serializer.data) #Y retornamos el objeto serializado
    
    elif request.method == 'PUT': #Si la peticion es PUT
        deserializer = MascotasSerializer(mascota, data=request.data) #Declaramos una variables para almacenar el objeto que nos manda el cliente o framework de frontend
        if deserializer.is_valid(): #Si el objeto es valido
            deserializer.save() #Guardamos el objeto
            return Response(deserializer.data) #Retornamos el objeto serializado y el estatus de creado
        
        #Si los datos no son validos
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # Si la peticion es DELETE
        mascota.delete() #Borramos la mascota
        return Response(status=status.HTTP_204_NO_CONTENT)
