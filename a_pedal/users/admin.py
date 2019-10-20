from django.contrib import admin

# Register your models here.

from users.models import Perfil

@admin.register(Perfil)
class Perfil_admin(admin.ModelAdmin):
    list_display = ('pk','user')