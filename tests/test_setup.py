from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from polls.models import Poll, Question, Choice, Answer, AuthID


class TestSetUp(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(username="name", password="pwsrd!@334FW", email='')
        self.token = Token.objects.create(user=self.admin)
        self.user = AuthID.objects.create(auth_id=777)
        self.api_token_authentication()

        AuthID.objects.create(auth_id=111)
        poll = Poll.objects.create(poll_name='name', description='description', end_date='2021-02-20')
        question1 = Question.objects.create(poll=poll, question_text='Why?', question_type=1)
        question2 = Question.objects.create(poll=poll, question_text='What?', question_type=2)
        question3 = Question.objects.create(poll=poll, question_text='Where?', question_type=3)
        choice1 = Choice.objects.create(question=question2, choice_text='choice1')
        Choice.objects.create(question=question2, choice_text='choice2')
        choice3 = Choice.objects.create(question=question3, choice_text='choice3')
        Choice.objects.create(question=question3, choice_text='choice4')
        choice5 = Choice.objects.create(question=question3, choice_text='choice5')
        # For question with text answer
        Answer.objects.create(poll=poll, question=question1, answer_text='answer', answered_by=self.user)
        # For question with one option
        Answer.objects.create(poll=poll, question=question2,
                              selected_option=choice1, answered_by=self.user)
        # For question with multiple choice
        Answer.objects.create(poll=poll, question=question3,
                              answered_by=self.user).selected_options.set((choice3, choice5))

    def api_token_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))