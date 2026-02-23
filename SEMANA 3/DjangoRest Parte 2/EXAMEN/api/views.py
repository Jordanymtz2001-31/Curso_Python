
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Denominacion
from .serializers import DenominacionesSerializers
from decimal import Decimal

#Funcion para listar las denominaciones
@api_view(['GET'])
def listar_denominaciones(request):
    denominaciones = Denominacion.objects.all() #Obtenemos todas las denominaciones y las asignamos a la variable
    serializer = DenominacionesSerializers(denominaciones, many=True) #Ahora en una variable alamcenamos la lista de denominaciones pero ya serializadas y el Many indicamso que es una coleccion (varios elementos)
    return Response(serializer.data) #Retornamos las respuesta en JSON

#Funcion para incializar el cajero
@api_view(['POST'])
def incializar_cajero(request):
    inicializar = Denominacion.inicializar_cajero() #Llamamos a la función para incializar el cajero
    return Response(inicializar)

#Funcion para retirar dinero del cajero y actualizar las denominaciones y hacer validaciones
@api_view(['POST'])
def retirar_dinero(request):
    monto = request.data.get('monto') #Obtenemos el monto que nos manda el cliente
    if monto is None or monto <= 0: #Si el monto es None o es menor o igual a 0
        return Response({'error': 'El monto debe ser mayor a 0.'}, status=status.HTTP_400_BAD_REQUEST) #Retornamos un error

    #Obtenemos el total de las denominaciones
    total_dinero = sum(denominacion.cantidad * denominacion.valor for denominacion in Denominacion.objects.all()) #Sumamos la cantidad de cada denominacion por su valor
    #Si el monto es mayor que el total de las denominaciones
    if monto > total_dinero:
        return Response({'error': 'Fondos insuficioentes.'}, status=status.HTTP_400_BAD_REQUEST) #Retornamos un error
    
    # Algoritmo GREEDY
    #Primero debemos de obtener el valor de las denominaciones pero en orden descendente (es decir de mayor a menor)
    #Decimos que es que sera una lista y lo almacenamos en una variable
    denoms = list(Denominacion.objects.order_by('-valor')) 
    desglose = [] #Declaramos una lista de desglose
    remaining = Decimal(str(monto)) #El remanente es el monto que nos manda el cliente
    
    #EJEMPLO DE QUIERO SACAR 200
    for denom in denoms: #Aqui obtenemos la denominacion recorriendo la lista para que cada valor de la denominacion sea evaluado con el monto del cliente
        if denom.valor > remaining: #Si el valor de la denominacion es mayor que 200
            continue #Entonces saltamos a la siguiente denominacion

        #Entonces obtenemos la cantidad minima de la denominacio 
        count = min(int(remaining / denom.valor), denom.cantidad) #Es decir  200/200 = 1, entonces la cantidad minima es 1 billete y con denom.cantidad obtenemos la cantidad de billetes que tenemos en el cajero

        if count > 0: #Si la cantidad es mayor a 0

            #Agregamos la denominacion al desglose
            desglose.append({
                'tipo': denom.tipo,
                'valor': float(denom.valor),
                'cantidad': count
            })

            #Restamos el valor de la denominacion por la cantidad
            remaining -= denom.valor * count #Es decir 200 - 200*1 = 0
            denom.cantidad -= count #Es decir 1 - 1 
            denom.save()
    
    if remaining > 0: #Si sobro dinero
        return Response({'error': 'No hay cambio exacto'}, status=400)
    
    #Retornamos el desglose con el total
    return Response({'desglose': desglose,'total': float(monto)})

#Funbcion para agregar dinero al cajero
@api_view(['POST'])
def depositar_dinero(request):
    recarga = request.data.get('recarga', []) #Obtenemos la cantidad que nos manda el cliente

    #En la recarga tenemos un diccionario con el valor y la cantidad
    """
    {
        "recarga": [
            {"valor": 100, "cantidad": 5},
            {"valor": 50, "cantidad": 10}
        ]
    }
    """
    for item in recarga: #Para obtener los elementos de la recarga tenemos que recorrerla (billete/moneda)

        try:
            denominacion = Denominacion.objects.get(valor=item['valor']) #Buscamos en las denominaciones el valor que coincida con el valor de la recarga
            denominacion.cantidad += item['cantidad'] #Aumentamos la cantidad de la denominacion
            denominacion.save() #Guardamos la denominacion
        except Denominacion.DoesNotExist: #Si no existe la denominacion
            return Response({'error': f'Denominación no válida ${item["valor"]} no existe. Valores disponibles: {[float(denominacion.valor) for denominacion in Denominacion.objects.all()]}'}, status=status.HTTP_400_BAD_REQUEST)

    denoms = Denominacion.objects.all() #Obtenemos todas las denominaciones
    serializer = DenominacionesSerializers(denoms, many=True) #Ahora en una variable alamcenamos la lista de denominaciones pero ya serializadas y el Many indicamso que es una coleccion (varios elementos
    return Response({'mensaje': 'Dinero agregado correctamente', 'denominaciones': serializer.data} )

