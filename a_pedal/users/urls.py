from django.urls import path

from users.views import PerfilTest,Login,SignUp

urlpatterns = [
    path('perfiles/',PerfilTest.as_view(),name='perfiles'),
    path('login/',Login.as_view(),name='login'),
    path('signup/',SignUp.as_view()),
]
