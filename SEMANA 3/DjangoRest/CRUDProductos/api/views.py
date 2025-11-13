from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productos
from .serializer import ProductoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def listar_y_guardar(request):
    if request.method == 'GET': #Si es un GET, lista.
        productos = Productos.objects.all()
        serializer = ProductoSerializer(productos, many = True) #Serializamos
        return Response(serializer.data)
    
    elif request.method == 'POST': #Si es un POST, guarda.
        serializer = ProductoSerializer(data = request.data) #Deserializamos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalles(request, id):
    #Buscamos el producto por su id
    try:
        producto = Productos.objects.get(pk = id)
    except Productos.DoesNotExist: #Si el producto no existe
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto) #Serializando
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductoSerializer(producto, data = request.data) #Deserializamos
        if serializer.is_valid():
            serializer.save() #Guardamos cambios en la bd
            return Response(serializer.data) #Retornamos un respuesta actualizada
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        producto.delete() #Se elimina
        return Response(status=status.HTTP_204_NO_CONTENT)