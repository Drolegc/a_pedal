from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#DJango users
from django.contrib.auth import (
    authenticate,
    password_validation
    )

from django.contrib.auth.models import User
#Modelo users
from users.models import Perfil


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):

        user = authenticate(username=data['username'],password=data['password'])
        print(type(user))
        if not user:
            raise serializers.ValidationError("Incorrecto!")
        
        print(Perfil.objects.get(user__username="test"))
        self.context['user'] = Perfil.objects.get(user=user)
        return data

    def create(self,data):
        token,created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'],token.key

class UserSignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        min_length=3,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8,max_length=64)
    password_conf = serializers.CharField(min_length=8,max_length=64)
    email = serializers.EmailField(validators=[])
    
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
        fields = ['username','password','email']

class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Perfil
        fields = '__all__'

