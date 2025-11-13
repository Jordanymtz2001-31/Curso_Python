from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria}"
    
    class Meta:
        db_table = 'Peliculas'
