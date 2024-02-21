from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UsersApiTests(APITestCase):

    def test_registration(self):
        url=reverse("registration")
        data = {"first_name":"first_name","last_name":"last_name","email":"email@email.com","password":"12345678"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("first_name"),"first_name")
        self.assertNotEqual(response.data,None)
        self.assertEqual(type(response.data.get("id")),int)