from django.db import models
from django.contrib.auth.models import AbstractUser

# Creamos una clase que herede de la clase AbstractUser para realizar la informacion de nuestro modelo
class Usuario(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('USER', 'Usuario normal'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='USER')
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creado = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Productos'