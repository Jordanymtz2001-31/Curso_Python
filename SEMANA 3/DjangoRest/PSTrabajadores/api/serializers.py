from rest_framework import serializers
from .models import Trabajadores, RespaldoTrabajadores

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajadores
        fields = '__all__'
        
class RespaldoTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespaldoTrabajadores
        fields = '__all__'