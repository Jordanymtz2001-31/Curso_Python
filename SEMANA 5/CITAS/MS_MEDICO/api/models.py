from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    id_cita = models.IntegerField()


    class Meta:
        db_table = 'medico'
    
    def __str__(self):
        return self.nombre
