from django.contrib import admin

# Register your models here.

from planes.models import Planes,Valoracion

@admin.register(Planes)
class Planes_admin(admin.ModelAdmin):
    list_display = ('pk','titulo','creador','imagen')

@admin.register(Valoracion)
class Valoracion_admin(admin.ModelAdmin):
    list_display = ('pk','user','like')