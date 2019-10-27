from django.shortcuts import render
from a_pedal.settings import SECRET_KEY
import jwt
#DRF
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
) 
from rest_framework.response import Response
from rest_framework import viewsets,status

#Model
from planes.models import Planes
from users.models import Perfil
from puntos.models import Punto
#Serializer
from planes.serializers import PlanSerializer,CrearPlanSerializer
#Permissions
from a_pedal.permissions import IsLogged
# Create your views here.


class PlanesViewSet(viewsets.ModelViewSet):

    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    lookup_field = 'id'
    permission_classes = [IsLogged]

    def create(self,request):
        data = request.data
        user = Perfil.objects.get(user__username=jwt.decode(data['token'],SECRET_KEY,algorithm='HS256')['user'])
        puntos = data.pop('puntos')
        data.pop('token')
        plan = Planes.objects.create(creador=user,**data)
        for punto in puntos:
            p = Punto.objects.create(**punto)
            plan.puntos.add(p)
        plan.save()
        return Response(PlanSerializer(plan).data,status=status.HTTP_201_CREATED)






""" A list of Planes """
class PlanesListView(ListAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    

""" Get a Plan from the id """
class PlanPorIdView(RetrieveAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    lookup_field = 'id'
    

""" Create a particular Plan """
class CrearPlanView(CreateAPIView):
    permission_classes = [IsLogged]
    queryset = Planes.objects.all()
    serializer_class = CrearPlanSerializer
