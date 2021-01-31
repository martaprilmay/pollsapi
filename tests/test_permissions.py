from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from polls.models import AuthID


class TestHasAnID(APITestCase):

    def test_create_auth_id(self):
        url = reverse('polls:create-id')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(response.data), int)
        self.assertEqual(AuthID.objects.count(), 1)
        self.assertEqual(response.data, AuthID.objects.get(pk=1).auth_id)

    def test_authentication_with_correct_value(self):
        AuthID.objects.create(auth_id=777)
        self.client.credentials(HTTP_AUTH_ID=777)
        url = reverse('polls:my-answers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_with_wrong_value(self):
        self.client.credentials(HTTP_AUTH_ID=7)
        url = reverse('polls:my-answers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_with_no_value(self):
        url = reverse('polls:my-answers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)