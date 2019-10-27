from django.db import models

# Create your models here.

class Punto(models.Model):
    creador = models.ForeignKey("users.Perfil", verbose_name=("creador"), on_delete=models.SET_NULL,null=True,blank=False)
    latitud = models.FloatField(blank=False,null=False)
    longitud = models.FloatField(blank=False,null=False)
    nombre = models.CharField(max_length=25,blank=False,null=False)
    descripcion = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.nombre,
            self.descripcion,
            self.latitud,
            self.longitud)