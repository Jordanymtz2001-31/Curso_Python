from django.test import TestCase
from .models import Carros
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class CarrosAPITest(TestCase):
    
    def setUp(self):
        #Creamos el cliente
        self.cliente = APIClient()
        #Creamos un objeto carro
        self.carro = Carros.objects.create(
            marca = "Toyota",
            modelo = "T123",
            anio = 2015,
            color = "Blanco",
            precio = 250000
        )
        #Definimos rutas
        self.url = '/carros/' #Listar y guardar
        self.detail_url = f"/carros/{self.carro.id}/" #Resto de funciones
        
    def test_listar_carros(self):
        #Peticion
        response = self.cliente.get(self.url)
        #Afirmaciones
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        
    def test_guardar_carros(self):
        data = {
            "marca": "Honda",
            "modelo": "Civic",
            "anio": 2020,
            "color": "Negro",
            "precio": 185000
        }
        
        #Peticion
        response = self.cliente.post(self.url, data, format = 'json')
        #Afirmaciones
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['marca'], 'Honda')

    def test_buscar_carro(self):
        response = self.cliente.get(self.detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['marca'], self.carro.marca)
        
    def test_actualizar_carro(self):
        data = {
            "marca": "VW",
            "modelo": "Jetta",
            "anio": 2010,
            "color": "Blanco",
            "precio": 200000
        }
        
        response = self.cliente.put(self.detail_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['modelo'], 'Jetta')
        
    def test_actualizacion_parcial(self):
        data = {
            "color": "Rojo"
        }
        
        response = self.cliente.patch(self.detail_url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['color'], 'Rojo')
        self.assertEqual(response.data['marca'], self.carro.marca)
        
    def test_eliminar_producto(self):
        response = self.cliente.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #Validamos que NO exista el carro despues de la aliminacion
        self.assertFalse(Carros.objects.filter(id = self.carro.id).exists())