from django.db import models

#Modelo de alumnos
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    grado = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)

    class Meta:
        db_table = 'Alumno'
