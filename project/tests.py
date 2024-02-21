from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken



class TokensApiTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(first_name="first_name", last_name="last_name",email="email@email.com", password="password")
        self.client.login(email="email@email.com", password="password")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_get_tokens(self):
        url=reverse("token_pair")
        response = self.client.post(url, {'email':self.user.email, "password": "password"})
        access = response.data.get("access")
        refresh = response.data.get("refresh")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access)
        self.assertIsNotNone(refresh)
        decoded_token = RefreshToken(refresh).payload
        self.assertEqual(decoded_token["email"], self.user.email)

    def test_get_refresh_tokens(self):
        url = reverse("token_refresh")
        data = {'email': self.user.email,
                   "password": "password",
                   "refresh":str(self.refresh_token)}
        response = self.client.post(url, data=data)

        access = response.data.get("access")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access)

