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
#Modelo users
from users.models import Perfil
#JWT
import jwt 
#Py
from datetime import timedelta

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8,max_length=64)

    def validate(self,data):
        user = authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Incorrecto!")
        if not Perfil.objects.get(user=user).activo:
            raise serializers.ValidationError("No esta activo aun...")
        return data

    def create(self,data):
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user':data['username'],
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
        exclude = ['id']
