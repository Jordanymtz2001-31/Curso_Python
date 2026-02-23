from django.db import models

# Creamos el modelo de Mascotas
class Mascotas(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.IntegerField()
    especie = models.CharField(max_length=50)

    def __str__(self):
        return f"Mascota: {self.nombre} - Edad: {self.edad} - Peso: {self.peso} - Especie: {self.especie}"
