from django.shortcuts import render

#DRF
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
) 
#Model
from planes.models import Planes
#Serializer
from planes.serializers import PlanSerializer
#Permissions
from a_pedal.permissions import IsLogged
# Create your views here.


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
    serializer_class = PlanSerializer
