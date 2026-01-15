#Aqui vamos a crear un metodo para que Autocree un empleado

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Empleado


@receiver(post_save, sender=User)
def crear_empleado(sender, instance, created, **kwargs): # El sender es el modelo User y el instance es el objeto creado
    if created and not hasattr(instance, 'empleado'):
        Empleado.objects.create(
            user=instance, 
            nombre = instance.get_full_name() or instance.username,
            edad = 25, #Por default
            ciudad = 'Puebla',
            puesto = 'Empleado',
            departamento_id = 1,
            rol = 'empleado'
            )