from django.db import models

# Create your models here.
class Postres(models.Model):
    id_postre = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    class Meta:
        db_table = 'POSTRES'
