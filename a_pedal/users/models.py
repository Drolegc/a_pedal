from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.user)


# Create your models here.
