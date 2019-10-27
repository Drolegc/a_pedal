#DRF
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
) 

#Permissions
from a_pedal.permissions import IsLogged
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
    permission_classes = [IsLogged]
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer
    
