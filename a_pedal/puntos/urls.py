from django.urls import path,include

from puntos.views.punto_view_set import PuntoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',PuntoViewSet,basename="punto")

urlpatterns = [
    path('',include(router.urls)),
]
