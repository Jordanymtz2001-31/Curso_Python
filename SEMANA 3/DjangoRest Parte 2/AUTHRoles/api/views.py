from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAdmin, IsUser, IsAdminOrUser
from .models import Usuario, Producto
from .serializers import UsuarioSerializer, ProductoSerializer
from rest_framework.decorators import api_view, permission_classes


# Creamos la vista para el registro de usuario
class ResgistroView(APIView):
    permission_classes = [AllowAny] #Acceso publico
    # Creamos el metodo post para el registro de usuario
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data) #Declaramos una variables para almacenar el objeto que nos manda el cliente o framework de frontend
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado con exito!'})
        return Response(serializer.errors, status=400)

#Creamos una clase para Productos y hacer sus funciones para las vistas junto con sus permisos (Admin, User)
class ProductoView(APIView):

    """

    method = self.request.method  # DRF pasa ESTO automáticamente

    Si queremos cambiar o colocar explicitamente que persmisosn entonces ocupamos el if, dependiendo del metodo

    def get_permissions(self):
        if self.request.method == 'POST':    # CAMBIO POST
            return [IsUser()]               # SOLO USER puede crear
            
        elif self.request.method == 'PUT' or self.request.method == 'DELETE':  # ← CAMBIO PUT/DELETE
            return [IsAdmin()]              # SOLO ADMIN puede modificar
            
        return [IsAdminOrUser()]        # ← GET: ADMIN+USER (por defecto)

    def get(self, request):         # ADMIN+USER (defecto)
    def post(self, request):        # USER (if cambió el permiso)
    def put(self, request, pk):     # ADMIN (if cambió el permiso)
    """
    def get_permissions(self):
        """Controla permisos por método HTTP"""
        if self.request.method == 'POST':
            permission_classes = [IsUser]           # Crear: SOLO USER
        elif self.request.method in ['PUT', 'DELETE']:
            permission_classes = [IsAdmin]          # Editar/Eliminar: SOLO ADMIN
        elif self.request.path.endswith('buscar_por_nombre'): # Si la url termina con buscar_por_nombre
            permission_classes = [IsUser] # Buscar: SOLO USER
        else:  # GET
            permission_classes = [IsAdminOrUser]    # Listar: ADMIN+USER
            
        return [permission() for permission in permission_classes] #Retornamos un array con los permisos, el cual se pasa a la vista
    def get(self, request):         # ADMIN+USER
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    # Ahora SÍ bloquea correctamente
    def post(self, request):        # SOLO USER
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Producto creado!'}, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, id):     # SOLO ADMIN
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=404)
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Producto actualizado!'})
        return Response(serializer.errors, status=400)

    def delete(self, request, id):  # SOLO ADMIN
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()
            return Response({'mensaje': 'Producto eliminado!'})
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=404)
        
    #Metodo Personalizado para buscar por nombre del producto en la busqueda por medio de parametro
    def buscar_por_nombre(self, request):

        #Busqueda por parametro con query_params
        nombre = request.query_params.get('nombre', None) #Aqui definimos el parametro que queremos buscar que es nombre, esto en Postman
        
        if nombre: #Si existe el nombre
            producto = Producto.objects.get(nombre__iexact = nombre) #Obtenemos el nombre exacto y lo guardamos en una variable

            serializers = self.get_serializer(producto) #Despues el producto se lo pasamos a la serializados y lo guardamos en una variable
            return Response(serializers.data) #Y damos como respuesta al cliente
        
        return Response({'error': 'Producto no encontrado'}, status=400)
