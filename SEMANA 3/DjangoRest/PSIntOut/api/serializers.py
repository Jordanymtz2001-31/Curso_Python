from rest_framework import serializers
from .models import Postres

class PostresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Postres
        fields = '__all__'