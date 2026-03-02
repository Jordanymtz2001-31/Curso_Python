from rest_framework.test import APITestCase
from .models import Usuario

class RegistroAPITest(APITestCase):
    
    def test_registro(self):
        # Creamos un usuario
        data = {
            "username": "Dany",
            "password": "12345678",
            "rol": "USER"
        }
        # Hacemos una peticion de tipo post y le pasamos la url y el JSON
        response = self.client.post('/registro/', data)

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Usuario.objects.filter(username='Dany').exists()) # Verificamos que el usuario se haya creado

        usuario = Usuario.objects.get(username='Dany') #Recuperamos el usuario
        self.assertTrue(usuario.check_password('12345678')) #Para verificar que la contraseña no este almacenada en texto plano

class BienvenidoAPITest(APITestCase):
    def test_bienvenido(self):
        response = self.client.get('/bienvenida/')

        # Hacemos validaciones o Assert (Afirmaciones)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mensaje'], 'Bienvenido al sistema!')

class ConfigAdminAPITest(APITestCase):

    #Creamos 2 usuarios de la clase Usuario para poder hacer pruebas del acceso para ambos
    def setUp(self):#El setUp se ejecuta antes de cada prueba
        self.admin = Usuario.objects.create_user(username='Admin', password='12345678', rol='ADMIN')

        self.user = Usuario.objects.create_user(username='User', password='12345678', rol='USER')

        self.url = '/config/'

    def test_config_acceso_correcto(self):
        #Forzamos authenticacion con ADMIN
        self.client.force_authenticate(user = self.admin)

        response = self.client.get(self.url)#Hacemos una peticion de tipo GET

        self.assertEqual(response.status_code, 200)
        
    def test_config_acceso_denegado(self):
        #Autehticacion como usuario
        self.client.force_authenticate(user = self.user)

        response = self.client.get(self.url) #Hacemos una peticion de tipo GET

        self.assertEqual(response.status_code, 403)

class InfoUserAPITest(APITestCase):

    #Metodo que se ejecuta antes de cada prueba, el cual crea 2 usuarios
    def setUp(self):
        self.admin = Usuario.objects.create_user(username='Admin', password='12345678', rol='ADMIN')

        self.user = Usuario.objects.create_user(username='User', password='12345678', rol='USER')

        self.url = '/info/'

    #Metodo de prueba para acceder a la informacion por parte del user el cual debe ser correcto
    def test_info_acceso_correcto(self):
        #Forzamos authenticacion con USER, le pasamos el user que creamos
        self.client.force_authenticate(user = self.user)

        response = self.client.get(self.url) #Hacemos una peticion de tipo GET junto con la url

        self.assertEqual(response.status_code, 200)

    #Metodo de prueba para acceder a la informacion por parte del admin el cual debe ser Incorrecto por que no tiene permiso
    def test_info_acceso_denegado(self):
        #Forzamos authenticacion con ADMIN, le pasamos el admin que creamos
        self.client.force_authenticate(user = self.admin)

        response = self.client.get(self.url) #Hacemos una peticion de tipo GET junto con la url

        self.assertEqual(response.status_code, 403)

class AyudaAdminUserAPITest(APITestCase):

    #Metodo que se ejecuta antes de cada prueba, el cual crea 2 usuarios
    def setUp(self):
        self.admin = Usuario.objects.create_user(username='Admin', password='12345678', rol='ADMIN')

        self.user = Usuario.objects.create_user(username='User', password='12345678', rol='USER')

        self.url = '/ayuda/' #Definimos la url

    #Metodo de prueba para acceder a la informacion por parte del admin el cual debe ser correcto
    def test_ayuda_acceso_admin(self):
        #Forzamos authenticacion con ADMIN, le pasamos el admin que creamos
        self.client.force_authenticate(user = self.admin)

        response = self.client.get(self.url) #Hacemos una peticion de tipo GET junto con la url

        self.assertEqual(response.status_code, 200)

    #Metodo de prueba para acceder a la informacion por parte del user el cual debe ser Correcto por que ambos tienen permiso
    def test_ayuda_acceso_user(self):
        #Forzamos authenticacion con USER, le pasamos el user que creamos
        self.client.force_authenticate(user = self.user)

        response = self.client.get(self.url) #Hacemos una peticion de tipo GET junto con la url

        self.assertEqual(response.status_code, 200)