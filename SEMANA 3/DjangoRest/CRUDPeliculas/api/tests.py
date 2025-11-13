from django.test import TestCase
from django.urls import reverse
from .models import Pelicula
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class PeliculaAPITest(APITestCase):
    
    def setUp(self):
        
        self.pelicula1 = Pelicula.objects.create(
            nombre = "El padrino",
            categoria = "Crimen",
            director = "John Smith"
        )
        
        self.pelicula2 = Pelicula.objects.create(
            nombre = "Saw",
            categoria = "Terror",
            director = "Juan Perez"
        )
        
        self.pelicula3 = Pelicula.objects.create(
            nombre = "El aro",
            categoria = "Terror",
            director = "Luis Sanchez"
        )
        
        #Construimos las rutas usando la funcion reverse() que recupera dinamicamente las URLS a partir de su nombre en lugar de rutas hardcodeadas - manuales
        self.url = reverse('peliculas_url-list') #Ruta para listar y crear
        self.url_detail = reverse('peliculas_url-detail', args=[self.pelicula3.id])
        #Rutas hardcode
        self.url_categoria = '/peliculas/buscar-categoria/'
        self.url_buscar_nombre = f"/peliculas/buscar-nombre/{self.pelicula2.nombre}/"
        #Ruta de prueba para buscar por nombre inexistente
        self.url_buscar_nombre_inexistente = f"/peliculas/buscar-nombre/Avatar/"
        
    def test_listar(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 3)
        
    def test_editar_parcial(self):
        data = {
            "categoria": "Misterio"
        }
        
        response = self.client.patch(self.url_detail, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pelicula3.refresh_from_db() #Confirmar la actualizacion del objeto "pelicula3" en la bd simulada
        self.assertEqual(self.pelicula3.categoria, 'Misterio')
        
    def test_categoria(self):
        response = self.client.get(self.url_categoria, {'categoria': 'Terror'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) == 2)
        
    def test_sin_categoria(self):
        response = self.client.get(self.url_categoria)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Error', response.data)
        
    def test_buscar_nombre(self):
        response = self.client.get(self.url_buscar_nombre)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.pelicula2.nombre)
        
    def test_buscar_nombre_inexistente(self):
        response = self.client.get(self.url_buscar_nombre_inexistente)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('Error', response.data)
        
    
