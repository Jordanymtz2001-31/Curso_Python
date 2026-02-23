from django.db import models

# Create your models here.
class Computadora(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ram = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    #Creamos una class Meta para definir el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'Computadora'