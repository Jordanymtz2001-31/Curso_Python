from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstractUser es una clase abstracta que funciona como plantilla base, ya tiene todos los campos del modelo USER de Django y es personalizable.
class Usuario(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('USER', 'Usuario normal'),
    )
    
    #Agregamos el campo rol al usuario
    rol = models.CharField(max_length=10, choices=ROLES, default='USER')
    
    def __str__(self):
        return self.username
