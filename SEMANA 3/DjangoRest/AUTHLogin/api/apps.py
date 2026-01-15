from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Indicamos que la base de datos sera de tipo BigAutoField, esto quiere decir que la base de datos se creara de manera automatica
    name = 'api'

    #Metodo para activar la señal que ayudara a crear el empleado
    def ready(self):
        import api.signals