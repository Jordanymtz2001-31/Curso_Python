from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    class Meta:
        db_table = 'PERSONAS'