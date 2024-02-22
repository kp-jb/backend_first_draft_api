from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Record

class RecordsApiTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(first_name="first_name", last_name="last_name",email="email@email.com", password="password")
        self.resume = Record.objects.create(
            name = "resume_name",
            content = "resume_content",
            is_resume = True,
            owner= self.user
        )
        self.client.login(email="email@email.com", password="password")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_get(self):
        url = reverse('record_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        records = response.data
        self.assertEqual(len(records), 1)
        self.assertContains(response, self.resume)

    def test_get_detailed(self):
        url = reverse('record_detail', kwargs={'pk':self.resume.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.resume)

    def test_resume_post(self):
        url = reverse("record_list")
        data = {
            "name" : "resume_name2",
            "content" : "resume_content2",
            "is_resume" : True,
            "owner": self.user.pk
        }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["is_resume"], True)

    def test_cover_letter_post(self):
        url = reverse("record_list")
        data = {
            "name" : "cover_letter_name",
            "content" : "cover_letter_content",
            "is_resume" : False,
            "owner": self.user.pk
        }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["is_resume"], False)

    def test_resume_put(self):
        url = reverse("record_detail", kwargs={"pk":self.resume.pk})
        data = {
            "name" : "resume_name_edited",
            "content" : "resume_content_edited",
            "is_resume" : True,
            "owner": self.user.pk
        }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"],"resume_name_edited")

    def test_delete(self):
        url = reverse("record_detail", kwargs={"pk":self.resume.pk})
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.delete(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)