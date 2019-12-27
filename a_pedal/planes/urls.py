from django.urls import path,include

from planes.views.planes_view_set import PlanesViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'planes',PlanesViewSet,basename='planes')

urlpatterns = [
    path('',include(router.urls)),

]
