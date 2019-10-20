from django.contrib import admin

# Register your models here.

from puntos.models import Punto

@admin.register(Punto)
class Punto_admin(admin.ModelAdmin):
    list_display = ('pk','latitud','longitud','nombre','descripcion')
