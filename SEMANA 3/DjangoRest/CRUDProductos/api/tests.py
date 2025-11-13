from django.test import TestCase
from .models import Productos
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class ProductosAPITest(TestCase):
    #Esta funcion se va a ejecutar SIEMPRE antes de cada prueba
    def setUp(self):
        #Creamos un cliente para las pruebas, simula las peticiones HTTP
        self.client = APIClient() 
        
        #Instanciamos un objeto para las pruebas en la BD SIMULADA
        self.producto = Productos.objects.create(
            nombre = "Manzanas",
            descripcion = "Caja de manzanas rojas",
            precio = 169.99,
            stock = 10
        )
        
        #Definimos las rutas
        self.url = '/producto/' #URL para listar y guardar
        # http://localhost:8000/producto/
        
        #URL para editar, eliminar y buscar
        self.url_detail = f"/producto/{self.producto.id}/"
        # http://localhost:8000/producto/1/
        
    def test_listar_productos(self):
        # "respuesta" es igual a la peticion simulada de tipo GET a la "url"
        respuesta = self.client.get(self.url)
        
        #Comprobacion con ASSERTS
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK) # a == b : TRUE
        self.assertGreaterEqual(len(respuesta.data), 1) #a >= b : TRUE
        
    def test_guardar_producto(self):
        #Creo un nuevo producto para guardar
        producto_nuevo = {
            "nombre": "Uvas",
            "descripcion": "Bolsa de 2kg de uvas verdes",
            "precio": 99.99,
            "stock": 5
        }
        
        #Simulando la peticion http de tipo POST a la "url", le mandamos el "producto_nuevo" como cuerpo de la peticion, le indicamos el formato en el que se envia "json" y guardamos la respuesta http en la variable "response".
        response = self.client.post(self.url, producto_nuevo, format="json")
        
        #AFIRMACIONES
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], "Uvas")
        
    def test_buscar_producto(self):
        response = self.client.get(self.url_detail)
        
        #Afirmaciones
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.producto.nombre)
        
    def test_editar_producto(self):
        producto_actualizado = {
            "nombre": "Sandia",
            "descripcion": "Sandia completa de 6kg",
            "precio": 49.99,
            "stock": 15
        }
        
        response = self.client.put(self.url_detail, producto_actualizado, format="json")
        
        #Afirmaciones
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], "Sandia") #a == b
        self.assertNotEqual(response.data['nombre'], "Manzanas") # a != b
        
    def test_eliminar_producto(self):
        response = self.client.delete(self.url_detail)
        
        #Afirmaciones
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        #Comprobamos que al intentar Buscar el producto ya NO EXISTA
        with self.assertRaises(Productos.DoesNotExist):
            Productos.objects.get(pk = self.producto.id)
        