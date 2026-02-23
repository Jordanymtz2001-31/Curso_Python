from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Huesped, Reserva
from .serializers import HuespedSerializer, ReservaSerializer

# CRUD HUESPEDES
@api_view(['GET'])
def huesped_list(request):
    huespedes = Huesped.objects.filter(activo=True)#Obtenemos todos los huespedes activos uy los guardamos en una variable
    serializer = HuespedSerializer(huespedes, many=True) #Ahora en una variable alamcenamos la lista de huespedes pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
    return Response(serializer.data) #El data significa los datos que se mandaran como respuesta al cliente

@api_view(['POST'])
def huesped_create(request):
    serializer = HuespedSerializer(data=request.data) #Obtenemos los datos que nos manda el cliente con la peticion, se los passamos al serializador para que lo deserialice y lo guarde en una variable
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) #Si los datos son validos los guardamos y retornamos el objeto serializado
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Si los datos no son validos retornamos los errores

@api_view(['PUT', 'PATCH'])
def huesped_update(request, id): #Recibimos el pk de la peticion
    huesped = get_object_or_404(Huesped, id=id) #Buscamos el huesped por su id con get_object_or_404
    serializer = HuespedSerializer(huesped, data=request.data, partial= request.method == 'PATCH') #Declaramos una variables para almacenar el objeto que nos manda el cliente o framework de frontend
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) #Retornamos el objeto serializado si es valido
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Retornamos los errores en caso de que no sea valido

@api_view(['DELETE'])
def huesped_delete(request, id):
    obj = get_object_or_404(Huesped, id=id) #Buscamos el huesped por su id
    obj.activo = False 
    obj.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD RESERVAS
@api_view(['GET'])
def reserva_list(request):
    reservas = Reserva.objects.filter(activo=True) #Obtenemos todas las reservas activas y las guardamos en una variable
    serializer = ReservaSerializer(reservas, many=True) #Ahora en una variable alamcenamos la lista de reservas pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
    return Response(serializer.data) #El data significa los datos que se mandaran como respuesta al cliente

@api_view(['POST'])
def reserva_create(request):
    serializer = ReservaSerializer(data=request.data) #Obtenemos los datos que nos manda el cliente con la peticion, se los passamos al serializador para que lo deserialice y lo guarde en una variable
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) #Si los datos son validos los guardamos y retornamos el objeto serializado
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Si los datos no son validos retornamos los errores

@api_view(['PUT', 'PATCH'])
def reserva_update(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    serializer = ReservaSerializer(reserva, data=request.data, partial=request.method == 'PATCH')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Metodo para cancelar una reserva sin eliminarla
@api_view(['DELETE'])
def reserva_cancel(request, id):
    obj = get_object_or_404(Reserva, id=id)
    obj.activo = False
    obj.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

# BÚSQUEDAS
@api_view(['GET'])
def reservas_por_huesped(request, huesped_id):
    #Metodo para listar las reservas de un huesped
    
    reservas = Reserva.objects.filter(huesped_id=huesped_id, activo=True)
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def huesped_por_nombre(request):
    #Metodo para listar los huespedes por su nombre

    nombre = request.query_params.get('nombre', '')
    huespedes = Huesped.objects.filter(nombre__icontains=nombre, activo=True)#Con icontains hacemos que se busque en cualquier parte del string sea mayuscula o minuscula
    serializer = HuespedSerializer(huespedes, many=True) #Ahora en una variable alamcenamos la lista de huespedes pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
    return Response(serializer.data)

@api_view(['GET'])
def reservas_por_fecha(request):
    #Metodo para listar las reservas por fecha

    fecha = request.query_params.get('fecha', '')
    reservas = Reserva.objects.filter(fecha_entrada__icontains=fecha, activo=True)
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)
