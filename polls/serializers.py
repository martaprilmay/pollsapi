from rest_framework import serializers

from .models import Poll, Question, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'