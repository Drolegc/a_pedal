from django.shortcuts import render

#DRF

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
) 

#Model
from puntos.models import Punto

#Serializer
from puntos.serializers import PuntoSerializer
# Create your views here.


""" Get a list of Points """
class PuntosListView(ListAPIView):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer

""" Get a point from the id """
class PuntoPorIdView(RetrieveAPIView):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer
    lookup_field = 'id'

""" Create a particular point """
class CrearPuntoView(CreateAPIView):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer
    
