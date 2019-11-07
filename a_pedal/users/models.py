from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.user)

class GoogleUser(models.Model):
    perfil = models.OneToOneField("users.Perfil",on_delete=models.CASCADE)

# Create your models here.
