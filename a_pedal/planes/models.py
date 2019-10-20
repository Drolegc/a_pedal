from django.db import models

#Models

from users.models import Perfil
from puntos.models import Punto

# Create your models here.

class Valoracion(models.Model):
    user = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    like = models.BooleanField()

class Planes(models.Model):
    titulo = models.CharField(max_length=15,blank=True)
    likes = models.ManyToManyField(Valoracion)
    puntos = models.ManyToManyField(Punto)
    creador = models.ForeignKey(Perfil,on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(
            self.titulo,
            self.likes,
            self.puntos)

