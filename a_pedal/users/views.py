from django.shortcuts import render

#Models

from users.models import Perfil
from django.contrib.auth.models import User

#Serializers
from users.serializers import PerfilSerializer

#REST
from rest_framework import generics
#from rest_framework.permissions import IsAdminUser

# Create your views here.

class PerfilTest(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
