from rest_framework import serializers

from .models import Poll, Question, Choice, Answer, AuthID


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'


class PollDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'poll_name', 'description')


class AnswerSerializer(serializers.ModelSerializer):
    selected_options = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'


class AuthIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthID
        fields = '__all__'
