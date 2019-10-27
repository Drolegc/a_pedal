from rest_framework import serializers

from puntos.models import Punto
from users.models import Perfil

import jwt

class PuntoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Punto
        exclude = ['id','creador']
    