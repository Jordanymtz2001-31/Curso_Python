from django.db import models

# Create your models here.
class Perfil(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nivel = models.CharField(max_length=50, default='Basico')
    
    def __str__(self):
        return f"Perfil: {self.usuario} - {self.nivel}"
    
    class Meta:
        db_table = 'Perfil'