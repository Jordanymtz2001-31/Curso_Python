from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Mascota
from rest_framework import status

# Creamos unitarias de prueba
class MascotaAPITest(TestCase): 
    
    # Creamos el metodo setUp que se ejecutara antes de cada prueba
    def setUp(self):

        #Creamos un cliente para las pruebas, APICliente simula un cliente, en lugar de una peticion HTT y es Una clase de Django
        self.client = APIClient()

        #Creamos una mascota para hacer las puebas en la BD simulanda
        self.mascota = Mascota.objects.create(
            nombre = 'Firulais',
            especie = 'Perro',
            edad = 5,
            tamanio = 'Grande'
        )

        #Definimos URLS
        self.url = '/mascotas/listar_guardar/' #Url para listar y guardar mascotas
        self.url_detalles = f'/mascotas/detalle/{self.mascota.id}/' #Url para ver detalles de la mascota
    

    #IMPORTANTE: Para las pruebas por convencion, Los metodos de prueba deben empezar con el prefijo "test_" sino no se ejecutaran

    # Creamos el metodo de prueba listar
    def test_listar(self):

        #La respuesta http es = a la peticion
        response = self.client.get(self.url)

        #Comprobamos que la respuesta es 200
        self.assertEqual(response.status_code, status.HTTP_200_OK) #El assertEqual es un metodo de la clase TestCase que nos permite comprobar que dos objetos son iguales

        #Comprobamos que la longitud de la respuesta es 1 (por que 1, por que solo tenemos una mascota en la BD simulada)
        self.assertGreaterEqual(len(response.data), 1)
        
        """
        assertEqual(): a == b : True
        assertNotEqual(): a != b : False
        assertGreater(): a > b : True
        assertGreaterEqual(): a >= b : True
        assertLess(): a < b : True
        assertLessEqual(): a <= b : True
        """

    # Creamos el metodo de prueba de guardar
    def test_guardar(self):

        #Creamos un JSON con los datos de la mascota para mandarlos en la peticion
        mascota_new = {
            "nombre": "Firu",
            "especie": "Perro",
            "edad": 5,
            "tamanio": "Grande"
        }

        #Hacemos una peticion de tipo post y guardamos la respuesta
        #Guardamos la respuesta de la peticion de tipo post y mandamos la url, los datos de la mascota y el formato
        response = self.client.post(self.url, mascota_new, format='json')


        #Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #Validamos el estatus de la peticion que sea creada
        self.assertEqual(response.data['nombre'], 'Firu') #Validamos que el nombre de la mascota sea Firu

    # Creamos el metodo de prueba de buscar
    def test_buscar(self):

        #Hacemos una peticion de tipo get con la url_detalles y guardamos la respuesta
        response = self.client.get(self.url_detalles)

        #Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Validamos el estatus de la peticion que sea 200
        self.assertEqual(response.data['nombre'], 'Firulais') #Validamos que el nombre de la mascota sea Firulais

    # Creamos el metodo para actualizar
    def test_actualizar(self):

        #Creamos un JSON con los datos de la mascota para mandarlos en la peticion
        mascota_actualizada = {
            "nombre": "Solobino",
            "especie": "Perro",
            "edad": 5,
            "tamanio": "Grande"
        }

        #Hacemos una peticion de tipo put con la url_detalles y mandamos los datos de la mascota y el formato y guardamos la respuesta
        response = self.client.put(self.url_detalles, mascota_actualizada, format='json')

        #Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_200_OK) #Validamos el estatus de la peticion que sea 200
        self.assertEqual(response.data['nombre'], 'Solobino') #Validamos que el nombre de la mascota ahora sea Solobino
        self.assertNotEqual(response.data['nombre'], 'Firulais') #Validamos que el nombre de la mascota no sea Firulais

    #Creamos el metodo de prueba de borrar
    def test_borrar(self):

        #Hacemos una peticion de tipo delete con la url_detalles y guardamos la respuesta
        response = self.client.delete(self.url_detalles)

        #Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) #Validamos el estatus de la peticion que sea 204

        with self.assertRaises(Mascota.DoesNotExist): #Validamos que la mascota no exista
            Mascota.objects.get(id=self.mascota.id) #Buscamos la mascota en la base de datos

