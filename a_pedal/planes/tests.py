from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase
# Create your tests here.

class testPlan(APITestCase):

    def test_create_match(self):
        url = ('http://127.0.0.1:8000/plan/nuevo/')
        data = {
            "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCIsImV4cCI6MTU3MjIyNzg2Nn0.1u2DdPLLwXwVQ4PvOH8kcTs_ZUzdUFtgNmGB3HBCSUo",
            "titulo":"tituloTest1",
            "puntos":[
                {
                  "latitud":0.2,
                  "longitud":9.88,
                  "nombre":"TesteoPy",
                  "descripcion":"descripcionPy",
                },
                {
                  "latitud":0.2,
                  "longitud":9.88,
                  "nombre":"TesteoPy",
                  "descripcion":"descripcionPy",
                }

            ]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

