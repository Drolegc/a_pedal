#DRF
from rest_framework.response import Response
from rest_framework import viewsets,status
#Settings
from a_pedal.settings import SECRET_KEY
#Permissions
from a_pedal.permissions import IsLogged
#Model
from puntos.models.punto import Punto
from users.models import Perfil
#Serializer
from puntos.serializers.punto_serializer import PuntoSerializer
#Utils
import jwt


class PuntoViewSet(viewsets.ModelViewSet):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer
    permission_classes = [IsLogged]

    def create(self,request):
        data = request.data
        user = Perfil.objects.get(user__username=jwt.decode(data['token'],SECRET_KEY,algorithm='HS256')['user'])
        data.pop('token')
        punto = Punto.objects.create(creador=user,**data)
        return Response(PuntoSerializer(punto).data,status=status.HTTP_201_CREATED)
