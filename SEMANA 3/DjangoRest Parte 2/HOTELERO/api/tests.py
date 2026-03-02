from rest_framework.test import APITestCase
from rest_framework import status
from .models import Huesped, Reserva
from .serializers import HuespedSerializer, ReservaSerializer

#PRUEBAS PARA HUESPEDES

class HuespedTest(APITestCase):

    def setUp(self):
        self.huesped = Huesped.objects.create(
            nombre = 'Juan',
            correo = 'd1lXt@example.com',
            telefono = '1234567890',
        )

        self.url_huesped_listar = "/listar/"
        self.url_huesped_guardar = "/guardar/"
        self.url_huesped_actualizar = f"/editar/{self.huesped.id}/"
        self.url_huesped_borrar = f"/eliminar/{self.huesped.id}/"
        self.url_huesped_buscar_nombre = "/huespedes/buscar/"
        


    def test_listar_huespedes(self):

        # Pasamos la peticion de tipo get con la url_huesped_listar y guardamos la respuesta
        response = self.client.get(self.url_huesped_listar)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Validamos el estatus de la peticion que sea 200
        self.assertGreaterEqual(len(response.data), 1) # Validamos que la longitud de la respuesta sea 1

    def test_guardar_huesped(self):
        # Creamos un JSON con los datos de la mascota para mandarlos en la peticion
        data = {
            "nombre": "Max",
            "correo": "d1lcXt@example.com",
            "telefono": "5235978563",
        }
        # Hacemos una peticion de tipo post y le pasamos la url_huesped_guardar, los datos de la mascota y el formato
        response = self.client.post(self.url_huesped_guardar, data)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Validamos el estatus de la peticion que sea 201
        self.assertEqual(Huesped.objects.count(), 2) # Validamos que la cantidad de huespedes sea 2

    def test_actualizar_huesped(self):
        huesped_parcial = {
            "nombre": "Mario"
        }

        response = self.client.patch(self.url_huesped_actualizar, huesped_parcial)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.huesped.refresh_from_db() # Actualizamos el huesped desde la base de datos
        self.assertEqual(self.huesped.nombre, 'Mario') # Validamos que el nombre del huesped sea Mario

    def test_eliminar_huesped(self):

        # Hacemos una peticion de tipo delete con la url_huesped_borrar y guardamos la respuesta
        response = self.client.delete(self.url_huesped_borrar)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.huesped.refresh_from_db() # Actualizamos el huesped desde la base de datos
        self.assertFalse(self.huesped.activo) # Validamos que el huesped no este activo

    def test_buscar_huesped(self):

        # Hacemos una peticion de tipo get con la url_huesped_buscar y guardamos la respuesta
        response = self.client.get(self.url_huesped_buscar_nombre)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Validamos el estatus de la peticion que sea 200
        self.assertEqual(len(response.data), 1) # Validamos que la longitud de la respuesta sea 1
        self.assertEqual(response.data[0]['nombre'], 'Juan') # Validamos que el nombre del huesped sea Juan

class ReservaTest(APITestCase):

    def setUp(self):
        
        self.huesped = Huesped.objects.create(
            nombre = 'Juan',
            correo = 'd1lXt@example.com',
            telefono = '1234567890',
        ) 

        self.reserva = Reserva.objects.create(
            fecha_entrada = '2023-01-01',
            fecha_salida = '2023-01-10',
            habitacion = 1,
            precio = 100.00,
            huesped = self.huesped,
        )

        self.url_reserva_listar = "/listarR/"
        self.url_reserva_guardar = "/crearR/"
        self.url_reserva_actualizar = f"/editarR/{self.reserva.id}/"
        self.url_reserva_borrar = f"/cancelar/{self.reserva.id}/"
        self.url_huesped_buscar_reservas_por_huesped = f"/reservas/huesped/{self.huesped.id}/"

    def test_guardar_pedido(self):
        # Creamos un JSON con los datos de la mascota para mandarlos en la peticion
        data = {
            "fecha_entrada": "2023-01-01",
            "fecha_salida": "2023-01-10",
            "habitacion": 1,
            "precio": 100.00,
            "huesped": self.huesped.id
        }
        # Hacemos una peticion de tipo post y le pasamos la url_huesped_guardar, los datos de la mascota y el formato
        response = self.client.post(self.url_reserva_guardar, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Validamos el estatus de la peticion que sea 201
        self.assertEqual(Reserva.objects.count(), 2) # Validamos que la cantidad de reservas sea 2

    def test_listar_pedidos(self):
        # Hacemos una peticion de tipo get con la url_huesped_listar y guardamos la respuesta    
        response = self.client.get(self.url_reserva_listar)

        self.assertEqual(response.status_code, status.HTTP_200_OK) # Validamos el estatus de la peticion que sea 200
        self.assertGreaterEqual(len(response.data), 1) # Validamos que la longitud de la respuesta sea 1

    """
    TEST FALTA VERIFICAR BIEN (ESTA INESTABLE JUNTO CON EL SERIALIZERS)

    def test_actualizar_reserva(self):
        # Creamos un JSON con los datos del pedido para mandarlos en la peticion de forma parcial
        data = {
            "habitacion": 2
        }

        response = self.client.patch(self.url_reserva_actualizar, data) # Hacemos una peticion de tipo patch

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # Validamos el estatus de la peticion que sea 200
        self.reserva.refresh_from_db() # Actualizamos el pedido desde la base de datos
        self.assertEqual(self.reserva.habitacion, 2) # Validamos que la habitacion del pedido sea 2
    """
    def test_eliminar_reserva(self):
        # Hacemos una peticion de tipo delete con la url_huesped_borrar y guardamos la respuesta
        response = self.client.delete(self.url_reserva_borrar)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.reserva.refresh_from_db() # Actualizamos el pedido desde la base de datos
        self.assertFalse(self.reserva.activo) # Validamos que el pedido no este activo

    def test_reserva_por_huesped(self):

        # Hacemos una peticion de tipo get con la url_huesped_buscar y guardamos la respuesta
        response = self.client.get(self.url_huesped_buscar_reservas_por_huesped)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Validamos el estatus de la peticion que sea 200
        self.assertEqual(len(response.data), 1) # Validamos que la longitud de la respuesta sea 1