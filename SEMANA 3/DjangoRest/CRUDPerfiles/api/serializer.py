from rest_framework import serializers
from .models import Perfil
""" 
ModelSerializer es una clase abstracta de DRF wue automatiza la serializacion.
"""
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil #Indicamos que modelo se serializara
        fields = '__all__' #TODOS los campos del modelo se van a serializar