from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#DJango users
from django.utils import timezone
from django.contrib.auth import (
    authenticate,
    password_validation
    )
from a_pedal.settings import SECRET_KEY
from django.contrib.auth.models import User
#Custom authentication
from a_pedal.authentication import authenticate
#Modelo users
from users.models import Perfil,GoogleUser
#JWT
import jwt 
#Py
from datetime import timedelta
#Requests
import requests as Request

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self,data):

        user = authenticate(email=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Incorrecto!")
        if not Perfil.objects.get(user=user).activo:
            raise serializers.ValidationError("No esta activo aun...")
        return data

    def create(self,data):
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user':data['email'],
            'exp':int(exp_date.timestamp())
            }
        token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')

        #token,created = Token.objects.get_or_create(user=self.context['user'].user)
        return token.decode()

class UserSignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        min_length=3,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8,max_length=64,write_only=True)
    password_conf = serializers.CharField(min_length=8,max_length=64,write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    
    def validate(self,data):
        passwd = data['password']
        passwd_conf = data['password_conf']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Contrasenia no coincide.")

        password_validation.validate_password(passwd)
        return data

    def create(self,data):
        data.pop('password_conf')
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )

        Perfil.objects.create(user=user)

        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']

class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Perfil
        exclude = ['id','activo']

class GoogleSignUpSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self,data):
        url = 'https://oauth2.googleapis.com/tokeninfo?id_token='  
        
        with Request.Session() as Connection:
            valid_token = Connection.get(url + data['token'])
            valid_token = valid_token.json()

        try:
            #chequeo error:invalid token
            valid_token['sub']
        except:
            raise serializers.ValidationError("Id token invalido")

        return valid_token

    def create(self,data):

        user = User.objects.create_user(
            username = data['name'],
            password = 'GooglePassword'+data['sub'],
            email = data['email']
        )

        perfil = Perfil.objects.create(user=user,activo=True)
        GoogleUser.objects.create(perfil = perfil)

        #Crear JWT
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user':data['email'],
            'exp':int(exp_date.timestamp())
            }
        token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')

        #token,created = Token.objects.get_or_create(user=self.context['user'].user)
        return token.decode()

class GoogleLoginSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self,data):
        url = 'https://oauth2.googleapis.com/tokeninfo?id_token='  
        
        with Request.Session() as Connection:
            valid_token = Connection.get(url + data['token'])
            valid_token = valid_token.json()

        try:
            email = valid_token['email']
            password = 'GooglePassword'+valid_token['sub']

            user = authenticate(email=email,password=password)

            if not user:
                raise serializers.ValidationError("Usuario no registrado")

        except:
            raise serializers.ValidationError("Id token invalido")

        return valid_token

    def create(self,data):
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user':data['email'],
            'exp':int(exp_date.timestamp())
            }
        token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')

        #token,created = Token.objects.get_or_create(user=self.context['user'].user)
        return token.decode()

        
        
        