from django.db import models

#Modelo de Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    puesto = models.CharField(max_length=50)

    #Definimos la tabla
    class Meta:
        db_table = 'Empleado'