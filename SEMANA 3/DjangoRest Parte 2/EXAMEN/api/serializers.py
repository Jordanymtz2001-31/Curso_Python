from rest_framework import serializers
from api.models import Denominacion

class DenominacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Denominacion
        fields = '__all__'