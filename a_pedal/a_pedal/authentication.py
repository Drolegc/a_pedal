from django.db import models

from django.contrib.auth.models import User

""" Autenticacion con email """
def authenticate(email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None