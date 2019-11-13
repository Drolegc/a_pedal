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
    likes = models.ManyToManyField('planes.Valoracion',blank=True,default=None)
    puntos = models.ManyToManyField('puntos.Punto',related_name='punto')
    creador = models.ForeignKey('users.Perfil',on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="planes",blank=False)

    def __str__(self):
        return "{}".format(
            self.titulo
            )

    @property
    def creador__user(self):
        return self.creador.user.username

