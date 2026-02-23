from django.db import models

# Modelos de Hablitos
class Habitats(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) #Puede ser vacio
    completed = models.BooleanField(default=False) # Por defecto es falso
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_at']
        db_table = 'habitats'