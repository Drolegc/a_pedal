#DRF
from rest_framework import serializers
#Serializer
from puntos.serializers import PuntoSerializer
from users.serializers import PerfilSerializer
#Models
from planes.models import Planes
from users.models import Perfil
from puntos.models import Punto
#Settings
from a_pedal.settings import SECRET_KEY

#Utils
import jwt

class CrearPlanSerializer(serializers.Serializer):

    #Creador
    token = serializers.CharField(write_only=True)
    puntos = PuntoSerializer(many=True)
    titulo = serializers.CharField()

    def create(self,data):
        user = Perfil.objects.get(user__username=jwt.decode(data['token'],SECRET_KEY,algorithm='HS256')['user'])
        data.pop('token')
        puntos_set = data.pop('puntos')
        plan = Planes.objects.create(creador=user,**data)
        for punto in puntos_set:
            p = Punto.objects.create(**punto)
            plan.puntos.add(p)
        plan.save()
        return plan




class PlanSerializer(serializers.ModelSerializer):
    puntos = PuntoSerializer(many=True)
    #Tomar solo el nickname
    creador = serializers.StringRelatedField()
    

    class Meta:
        model = Planes
        fields = '__all__'

