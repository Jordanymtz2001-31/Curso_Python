from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pelicula
from .serializer import PeliculaSerializer

# Create your views here.
class PeliculaViewSets(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    
    # URL: http://localhost:8000/peliculas/buscar-categoria/
    
    #Funcion de busqueda por parametro
    @action(detail=False, methods=['get'], url_path='buscar-categoria')
    def buscar_por_categoria(self, request):
        #Busqueda por parametro "categoria"
        categoria = request.query_params.get('categoria', None)
        
        if categoria:
            peliculas = Pelicula.objects.filter(categoria__iexact = categoria)
            serializer = self.get_serializer(peliculas, many = True)
            return Response(serializer.data)
        
        return Response({'Error': 'Debes proporcionar una categoria'}, status=400)

     # URL: http://localhost:8000/peliculas/buscar-nombre/Titanic/
     
    """ 
     (?P<nombre>[^/.]+) esto es una EXPRESION REGULAR (regex)
     
     nombre - clave
     [] -  Tomas el valor que se encuentre dentro de los corchetes
     ^  -  negacion
     /. -  Caracteres no permitidos
     +  -  Una o mas veces de los carecteres permitidos
    """
     

    @action(detail=False, methods=['get'], url_path='buscar-nombre/(?P<nombre>[^/.]+)')
    def buscar_por_nombre(self, request, nombre):
        if nombre:
            try:
                pelicula = Pelicula.objects.get(nombre__icontains = nombre)
                serializer = self.get_serializer(pelicula)
                return Response(serializer.data)
            except Pelicula.DoesNotExist:
                return Response({'Error': 'No se encontro la pelicula con ese nombre'}, status=404)
            
        return Response({'Error': 'Debes proporcionar un nombre'}, status=400)