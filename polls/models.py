from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Poll(models.Model):
    poll_name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    TYPE = (
        (1, 'Text'),
        (2, 'Select'),
        (3, 'Choice'),
    )
    question_type = models.IntegerField(choices=TYPE, default=1)

    def __str__(self):
        return f'{self.question_text} ({self.question_type})'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', null=True, blank=True, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=64)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll', 'question', 'voted_by')


class Votes(models.Model):
    choices = models.ManyToManyField(Choice, related_name="selected_choices")
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    selected_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll', 'question', 'selected_by')


class Answer(models.Model):
    answer_text = models.CharField(max_length=128, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll', 'question', 'answered_by')


class AuthID(models.Model):
    auth_id = models.IntegerField(unique=True)

