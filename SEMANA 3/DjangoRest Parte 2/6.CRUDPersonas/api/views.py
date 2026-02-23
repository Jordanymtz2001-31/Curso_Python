from rest_framework import viewsets
from .serializers import PersonaSerializer
from .models import Persona
from rest_framework.decorators import action
from rest_framework.response import Response


# Definimos una clase donde contendra los metodos basicos con ayuda de viewSet
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    #El detail = False es que se va a aplicar para un solo objeto
    #El detail = True es que se va a aplicar para varios objetos

    #Metodo para buscar personas por ocupacion
    #http://localhost:8000/personas/buscar-ocupacion/?ocupacion=Estudiante
    @action(detail = False, methods = ['get']) 
    def buscar_ocupacion(self, request):

        #Busqueda por parametro con query_params
        #O esta la otra opcion de busqueda con request.GET
        ocupacion =request.query_params.get('ocupacion', None) #Aqui definimos el parametro que queremos buscar que es ocupacion, esto en Postman

        if ocupacion: #Si exiate la ocupacion
            personas = Persona.objects.filter(ocupacion__iexact = ocupacion) #Obtenemos las personas que coincidan con la ocupacion y las guardamos en una variable

            serializer = self.get_serializer(personas, many = True) #Despues la lista se lo pasamos a la serializados y los guardamos en una variable
            return Response(serializer.data) #Y damos como respuesta al cliente
        
        return Response({'error': 'Ocupacion no encontrada'}, status=400) #En caso de que no exista la ocupacion entonces damos como respuesta un error
    
    """
    Expresion Regular (REGEX)

    P<nombre> grupo con nombre, nombre es la clave de la variable
    [] Conjunto de caracteres permitidos
    ^ Negacion
    /. caracteres No permitidos
    + Un caracter o mas
    """

    #Metodo para buscar el nombre por medio de un parametro en la url
    #localhost:8000/personas/buscar-nombre/Pepe
    @action(detail=False, methods=['get'], url_path='buscar-nombre/(?P<nombre>[^/.]+)')
    def buscar_nombre(self, request, nombre = None): #Le asignamos none al parametro para que no de error
        if nombre: #Si existe el nombre buscado
            try: 
                persona = Persona.objects.get(nombre__icontains = nombre) #Buscamos la persona que coincida con el nombre de nuestro modelo y la guardamos en una variable
                serializer = self.get_serializer(persona) #Despues la persona se lo pasamos a la serializados y la guardamos en una variable
                return Response(serializer.data) #Y damos como respuesta al cliente
            except Persona.DoesNotExist:
                return Response({'error': 'Persona no encontrada'}, status=400)
            
        return Response({'Error' : 'Debe de proporcionar un nombre'}, status=400)