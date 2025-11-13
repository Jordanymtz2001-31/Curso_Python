from django.db import models

# Create your models here.
class Paises(models.Model):
    nombre = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)
    idioma = models.CharField(max_length=100)
    habitantes = models.IntegerField()
    forma_gobierno = [
        ('Republica', 'Republica'),
        ('Monarquia', 'Monarquia')
    ]
    gobierno = models.CharField(max_length=50, choices=forma_gobierno)
    
    def __str__(self):
        return f"{self.nombre} - {self.gobierno}"
    
    class Meta:
        db_table = 'paises' #Definimos el nombre de la tabla
