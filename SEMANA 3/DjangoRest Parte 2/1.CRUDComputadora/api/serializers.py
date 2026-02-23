from rest_framework import serializers
from api.models import Computadora 

#Creamos una clase que herede de la clase ModelSerializer para realizar la informacion de nuestro modelo
class CompuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora #Asociamos nuestro modelo con el serializador
        fields = '__all__'