from rest_framework import serializers
from .models import Huesped, Reserva
from django.core.exceptions import ValidationError

class HuespedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huesped
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        # huesped nuevo si viene en la petición
        huesped = data.get('huesped')

        # Si es una actualización (PATCH/PUT) ya existe instancia
        if self.instance is not None:
            # Si no mandaron huesped en el body, usa el de la reserva existente
            if huesped is None:
                huesped = self.instance.huesped
        # Si es creación (POST) y no mandan huesped, marca error
        else:
            if huesped is None:
                raise serializers.ValidationError({'huesped': 'Este campo es obligatorio.'})

        if not huesped.activo:
            raise serializers.ValidationError('No se puede crear reserva para huésped inactivo.')

        if data['fecha_salida'] <= data['fecha_entrada']:
            raise serializers.ValidationError('La fecha de salida debe ser posterior a la fecha de entrada.')
        
        # QUITA huesped del data para evitar duplicado
        data_sin_huesped = data.copy()
        data_sin_huesped.pop('huesped', None)
        
        reserva = Reserva(**data_sin_huesped, huesped=huesped)
        reserva.full_clean()
        
        return data
