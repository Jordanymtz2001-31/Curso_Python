from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    #Creamos un signal para el modelo Estudiante
    def ready(self):
        from . import signals #Importamos el modulo signals
