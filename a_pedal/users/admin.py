from django.contrib import admin

# Register your models here.

from users.models import Perfil,GoogleUser

@admin.register(Perfil)
class Perfil_admin(admin.ModelAdmin):
    list_display = ('pk','user','activo')

@admin.register(GoogleUser)
class Google_admin(admin.ModelAdmin):
    list_display = ('perfil',)