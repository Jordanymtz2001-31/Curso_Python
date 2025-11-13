from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    numero = models.CharField(max_length=15)
    id_cita = models.IntegerField()

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.nombre