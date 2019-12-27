from django.db import models

#Models

from users.models import Perfil

class Valoracion(models.Model):
    user = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    like = models.BooleanField()
