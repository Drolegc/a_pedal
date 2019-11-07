from django.urls import path,include

from users.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',PerfilViewSet,basename='perfil')

urlpatterns = [
    path('',include(router.urls)),
]
