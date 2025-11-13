from django.db import models

# Create your models here.

# models.Model es un clase abstracta que nos proporciona todas las funcionalidades basicas de una BD. 
class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.tipo}, {self.categoria}"
