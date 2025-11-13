from rest_framework import serializers
from django.contrib.auth.models import User

class RegistroSerializer(serializers.ModelSerializer):
    
    #Write_only = True indica que a contraseña entra pero no sale
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['username', 'password'] #Lista de campos que se serializaran
    
    #Sobreescribimos la funcion create desde la clase Model.Serializer
    #Esta funcion se ejecuta automaticamente cuando se llama a "serializer.save()"
    def create(self, validated_data):
        #validated_data es un diccionario con los datos validados por el serializador
        #Creamos un instancia del modelo User con el username validado
        user = User(username = validated_data['username'])
        
        #La funcion set_password aplica la encriptacion a la contraseña antes de guardalo
        user.set_password(validated_data['password'])
        
        #Guardamos en la bd
        user.save()
        
        return user