from rest_framework.permissions import BasePermission
from a_pedal.settings import SECRET_KEY

import jwt

class IsLogged(BasePermission):
    message = "Sesion apretada"
    def has_permission(self,request,view):
        print(view.action)
        if view.action in ['update','create']:
            try:
                token = request.data['token']
                jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
                return True
            except:
                return False
        return True
