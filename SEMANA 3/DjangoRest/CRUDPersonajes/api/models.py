from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categorias = [
        #BD             #Visible al usuario
        ('SuperHeroe', 'SuperHeroe'),
        ('Villano', 'Villano')
    ]
    categoria = models.CharField(max_length=50, choices=categorias)
    habilidades = [
        ('Fuerza', 'Fuerza'),
        ('Velocidad', 'Velocidad'),
        ('Magia', 'Magia'),
        ('Inteligencia', 'Inteligencia')
    ]
    habilidad = models.CharField(max_length=50, choices=habilidades)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'Personajes'
