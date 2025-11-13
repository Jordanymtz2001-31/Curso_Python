from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Empleado'
