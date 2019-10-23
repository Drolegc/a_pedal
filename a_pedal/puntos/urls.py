from django.urls import path

from puntos.views import (
    PuntosListView,
    PuntoPorIdView,
    CrearPuntoView,
    )

urlpatterns = [
    path('puntos/',PuntosListView.as_view()),
    path('<int:id>/',PuntoPorIdView.as_view()),
    path('crear/',CrearPuntoView.as_view()),
]
