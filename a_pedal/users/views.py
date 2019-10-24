from django.shortcuts import render

#Models

from users.models import Perfil
from django.contrib.auth.models import User

#Serializers
from users.serializers import (PerfilSerializer,
    LoginSerializer,
    UserSerializer,
    UserSignUpSerializer
    )

#REST
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
    )
from rest_framework.views import APIView

from rest_framework import status

#from rest_framework.permissions import IsAdminUser

# Create your views here.

class SignUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
        
class PerfilTest(ListAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class Login(APIView):

    def post(self,request,*args, **kwargs):
        
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save() 

        data = {
            'token':token,
        }
        
        return Response(data,status=status.HTTP_201_CREATED)