from rest_framework import serializers
from api.models import Mascota

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'