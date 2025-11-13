from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'rol']
        #No se muestra la contraseña en la respuesta
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        #Encriptamos la contraseña
        #make_password es una funcion de encriptacion que usa el algoritmo PBKDF2 
        validated_data['password'] = make_password(validated_data['password'])
        #Llamamos a la funcion create Original de la clase ModelSerializer
        return super().create(validated_data)