from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    tamanio = models.CharField(max_length=50, db_column = 'tamaño') #Aqui se cambia el nombre de la columna de la base de datos para que se llame tamanio

    class Meta:
        db_table = 'Mascota'
