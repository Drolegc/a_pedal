from rest_framework import serializers

from puntos.models import Punto

class PuntoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Punto
        exclude = ['id']