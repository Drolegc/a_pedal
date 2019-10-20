from django.urls import path

from users.views import PerfilTest

urlpatterns = [
    path('perfiles/',PerfilTest.as_view(),name='perfiles'),
]
