from django.db import models

# 
class Tarea(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] #Ordenar por la fecha de creacion de forma descendente de la mas reciente a la mas antigua
        db_table = 'tareas'