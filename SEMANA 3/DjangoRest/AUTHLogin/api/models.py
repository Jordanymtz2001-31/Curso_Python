from django.contrib.auth.models import User # Aqui importamos el modelo User que tiene Django
from django.db import models

#Creamos 2 modelos de Departamento y Empleados donde el Empleado se creara y estara realcionado con user
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    class Meta:
        db_table = 'departamento'

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Aqui estamos indicando que el empleado pertenece a un user
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #Aqui indicamos que el empleado pertenece a un departamento

    #Definimos los roles de un empleado
    ROLES = [
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('empleado', 'Empleado'),
    ]
    rol = models.CharField(choices=(ROLES), max_length=50, default='empleado')

    class Meta:
        db_table = 'empleado'
    def __str__(self):
        return self.nombre