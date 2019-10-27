from django.urls import path,include

from planes.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pvs',PlanesViewSet,basename='pvs')

urlpatterns = [
    path('',include(router.urls)),
    path('planes/',PlanesListView.as_view()),
    path('<int:id>/',PlanPorIdView.as_view()),
    path('nuevo/',CrearPlanView.as_view()),
]
