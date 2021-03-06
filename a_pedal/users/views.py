from django.shortcuts import render
#Models
from users.models import Perfil
from django.contrib.auth.models import User
#Serializers
from users.serializers import (PerfilSerializer,
    LoginSerializer,
    UserSerializer,
    UserSignUpSerializer,
    GoogleLoginSerializer,
    GoogleSignUpSerializer
    )
from rest_framework import serializers
#REST
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView
    )
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status


# Create your views here.

class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    lookup_field = 'user__username'

    def create(self,validated_data):
        return Response(data={"to_create":"/perfil/signup/"},status=status.HTTP_303_SEE_OTHER)
    
    def update(self,instance,validated_data):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class SignUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class Login(APIView):

    def post(self,request,*args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save() 

        data = {
            'token':token,
        }
        
        return Response(data,status=status.HTTP_201_CREATED)

class GoogleSignUp(APIView):

    def post(self,request,*args, **kwargs):

        serializer = GoogleSignUpSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'token':token
        }
        return Response(data,status=status.HTTP_201_CREATED)

class GoogleLogin(APIView):

    def post(self,request,*args, **kwargs):

        serializer = GoogleLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'token': token
        }
        
        return Response(data,status=status.HTTP_201_CREATED)
