from django.urls import path

from planes.views import *

urlpatterns = [
    path('planes/',PlanesListView.as_view()),
    path('<int:id>/',PlanPorIdView.as_view()),
    path('nuevo/',CrearPlanView.as_view()),
]
