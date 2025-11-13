from django.db import models

class Cita(models.Model):
    id_cita = models.IntegerField()
    motivo = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cita'

    def __str__(self):
        return self.motivo
