import json
from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory

from .models import Poll, Question, Choice, Answer, AuthID
from . import views


class TestPoll(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="name", password="pwsrd!@334FW", email='')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
        Poll.objects.create(poll_name='name', description='description', end_date='2021-02-20')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_all_polls_list_admin_authenticated(self):
        url = reverse('polls:polls-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_polls_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('polls:polls-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_poll_admin_authenticated(self):
        url = reverse('polls:poll-create')
        data = {'poll_name': 'name', 'end_date': '2021-02-20', 'description': 'description'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 2)
        self.assertEqual(Poll.objects.get(pk=1).poll_name, 'name')
        self.assertEqual(Poll.objects.get(pk=1).description, 'description')
        self.assertEqual(Poll.objects.get(pk=1).end_date, date(2021, 2, 20))
        self.assertEqual(Poll.objects.get(pk=1).start_date, date.today())

    def test_poll_detail_retrieve_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('polls:polls-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['poll_name'], 'name')
        self.assertEqual(response.data['description'], 'description')
        self.assertEqual(response.data['end_date'], '2021-02-20')
        self.assertEqual(response.data['start_date'], str(date.today()))

    def test_poll_update_by_admin(self):
        url = reverse('polls:polls-update', kwargs={'pk': 1})
        response = self.client.put(url, {'poll_name': 'new_name', 'end_date': '2021-02-21',
                                         'description': 'new_description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(json.loads(response.content), {'id': 1, 'poll_name': 'new_name', 'end_date': '2021-02-21',
        #                                                 'description': 'new_description'})

    def test_poll_update_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('polls:polls-update', kwargs={'pk': 1})
        response = self.client.put(url, {'poll_name': 'new_name', 'end_date': '2021-02-21',
                                         'description': 'new_description'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_poll_delete_by_admin(self):
        url = reverse('polls:polls-update', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Poll.objects.count(), 0)

    def test_poll_delete_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('polls:polls-update', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Poll.objects.count(), 1)


class TestQuestion(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="name", password="pwsrd!@334FW", email='')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        Poll.objects.create(poll_name='name', description='description', end_date='2021-02-20')
        Question.objects.create(poll=Poll.objects.get(pk=1), question_text='Why?', question_type=1)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_question_list(self):
        url = reverse('polls:question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

