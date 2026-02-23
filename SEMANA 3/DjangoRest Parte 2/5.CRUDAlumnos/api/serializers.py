from rest_framework import serializers
from api.models import Alumno

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'