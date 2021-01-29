from datetime import date

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Poll, Question, Choice
from .serializers import (PollDetailSerializer, PollListSerializer, QuestionSerializer, ChoiceSerializer,
                          VoteSerializer, VotesSerializer, AnswerSerializer)


class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollListSerializer(polls, many=True).data
        return Response(data)


class ActivePollsList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Poll.objects.filter(start_date__lte=date.today()).filter(end_date__gte=date.today())
        return queryset
    serializer_class = PollListSerializer


class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollDetailSerializer(poll).data
        return Response(data)


class QuestionList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = QuestionSerializer


class QuestionDetail(APIView):
    def get(self, request, pk, q_pk):
        question = get_object_or_404(Question, pk=q_pk)
        data = QuestionSerializer(question).data
        return Response(data)


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs["q_pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, q_pk, c_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': c_pk, 'question': q_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateVotes(APIView):
    serializer_class = VotesSerializer

    def post(self, request, pk, q_pk):
        selected_by = request.data.get("selected_by")
        choices = request.data.get("choices")
        data = {'question': q_pk, 'poll': pk, 'choices': choices, 'selected_by': selected_by}
        serializer = VotesSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAnswer(APIView):
    serializer_class = AnswerSerializer

    def post(self, request, pk, q_pk):
        answered_by = request.data.get("answered_by")
        answer_text = request.data.get("answer_text")
        data = {'question': q_pk, 'poll': pk, 'answer_text': answer_text, 'answered_by': answered_by}
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
