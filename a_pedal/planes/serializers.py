#DRF
from rest_framework import serializers
#Serializer
from puntos.serializers import PuntoSerializer
from users.serializers import PerfilSerializer
#Models
from planes.models import Planes

class PlanSerializer(serializers.ModelSerializer):
    puntos = PuntoSerializer(many=True)
    creador = PerfilSerializer()

    class Meta:
        model = Planes
        fields = '__all__'