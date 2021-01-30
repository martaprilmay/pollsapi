from collections import OrderedDict

from rest_framework import serializers

from .models import Poll, Question, Choice, Answer, AuthID


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
        extra_kwargs = {'selected_options': {'required': False, 'allow_null': True}}
        validators = []


class AnswerDetailSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='question_text', queryset=Question.objects.all())
    selected_option = serializers.SlugRelatedField(slug_field='choice_text', queryset=Choice.objects.all())
    selected_options = serializers.SlugRelatedField(slug_field='choice_text', many=True, queryset=Choice.objects.all())
    poll = serializers.SlugRelatedField(slug_field='poll_name', queryset=Poll.objects.all())
    answered_by = serializers.SlugRelatedField(slug_field='auth_id', queryset=AuthID.objects.all())

    class Meta:
        model = Answer
        fields = '__all__'

    def to_representation(self, instance):
        result = super(AnswerDetailSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


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


class AuthIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthID
        fields = '__all__'
