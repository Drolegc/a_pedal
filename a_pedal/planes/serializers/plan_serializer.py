#DRF
from rest_framework import serializers
#Serializer
from puntos.serializers.punto_serializer import PuntoSerializer
from users.serializers import PerfilSerializer
#Models
from planes.models.planes import Planes
from users.models import Perfil
from puntos.models.punto import Punto
#Settings
from a_pedal.settings import SECRET_KEY

#Utils
import jwt

class PlanSerializer(serializers.ModelSerializer):

    data_creador = PerfilSerializer(source='creador',read_only=True)

    class Meta:

        model = Planes
        fields = [
            'titulo',
            'likes',
            'puntos',
            'creador',
            'data_creador',
            #'imagen'
        ]
        extra_kwargs={'likes':{'read_only':True}}

    def create(self,data):

        print("Composicion de data {}\n".format(data))
        user = Perfil.objects.get(user__username=jwt.decode(data['token'],SECRET_KEY,algorithm='HS256')['user'])
        data.pop('token')
        puntos_set = data.pop('puntos')
        plan = Planes.objects.create(creador=user,**data)
        for punto in puntos_set:
            p = Punto.objects.create(**punto)
            plan.puntos.add(p)
        plan.save()
        return plan


