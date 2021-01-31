from rest_framework.test import APITestCase, APIRequestFactory

from . import views


class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory
        self.view =
