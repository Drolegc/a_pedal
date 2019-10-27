from django.urls import path,include

from planes.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',PlanesViewSet,basename='planes')

urlpatterns = [
    path('',include(router.urls)),

]
