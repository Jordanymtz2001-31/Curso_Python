from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completado = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha']
        db_table = 'Tareas'