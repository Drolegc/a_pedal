from django.db import models

# Create your models here.

class Punto(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.nombre,
            self.descripcion,
            self.latitud,
            self.longitud)