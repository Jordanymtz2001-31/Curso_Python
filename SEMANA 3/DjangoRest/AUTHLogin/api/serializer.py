from rest_framework import serializers
from .models import Departamento, Empleado
from django.contrib.auth.models import User

class DepartamentoSerializer(serializers.ModelSerializer): #ModelSerializer nos ofrece seleccionar todos los campos de jalo
    class Meta:
        model = Departamento
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.username', read_only=True) #Indicamos que queremos que se muestre el username de la tabla User
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True) #Indicamos que queremos que se muestre el username de la tabla User

    class Meta:
        model = Empleado
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    nombre = serializers.CharField()
    edad = serializers.IntegerField()
    ciudad = serializers.CharField()
    puesto = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user