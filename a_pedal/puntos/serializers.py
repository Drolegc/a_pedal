from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from puntos.models import Punto

class PuntoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Punto
        fields = '__all__'