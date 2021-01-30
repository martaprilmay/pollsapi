from datetime import date
from random import randint

from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from .models import Poll, Question, Choice, AuthID
from .permissions import HasAnID
from .serializers import (PollDetailSerializer, PollListSerializer, QuestionSerializer, ChoiceSerializer,
                          AnswerSerializer, AuthIDSerializer)


class PollCreate(generics.CreateAPIView):
    """ Admin creates a Poll object via POST """
    serializer_class = PollDetailSerializer
    permission_classes = (IsAdminUser,)


class PollUpdate(generics.RetrieveUpdateDestroyAPIView):
    """ Admin updates/deletes a Poll object via PUT, DELETE """
    queryset = Poll.objects.all()
    serializer_class = PollDetailSerializer
    permission_classes = (IsAdminUser,)


class PollList(generics.ListCreateAPIView):
    """ A list of all Polls (incl. future and expired).
        Available only to Admin via GET
    """
    queryset = Poll.objects.all()
    serializer_class = PollListSerializer
    permission_classes = (IsAdminUser,)


class ActivePollsList(generics.ListCreateAPIView):
    """ A list of active Polls (with id, name and description).
        Available to anyone via GET
    """
    queryset = Poll.objects.filter(start_date__lte=date.today()).filter(end_date__gte=date.today())
    serializer_class = PollListSerializer


class PollDetail(APIView):
    """ A Poll detailed view (with all fields + questions + choices).
        Available to anyone via GET
    """
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollDetailSerializer(poll).data
        return Response(data)


class QuestionCreate(generics.CreateAPIView):
    """ Admin creates a Question object via POST """
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)


class QuestionUpdate(generics.RetrieveUpdateDestroyAPIView):
    """ Admin updates/deletes a Question object via PUT, DELETE """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)


class QuestionList(generics.ListCreateAPIView):
    """ A list of all Questions of a specific Poll.
        Available to anyone via GET
    """
    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = QuestionSerializer


class QuestionDetail(APIView):
    """ A Poll detailed view (with all fields + choices).
        Available to anyone via GET
    """
    def get(self, request, pk, q_pk):
        question = get_object_or_404(Question, pk=q_pk)
        data = QuestionSerializer(question).data
        return Response(data)


class ChoiceCreate(generics.CreateAPIView):
    """ Admin creates a Choice object via POST """
    serializer_class = ChoiceSerializer
    permission_classes = (IsAdminUser,)


class ChoiceUpdate(generics.RetrieveUpdateDestroyAPIView):
    """ Admin updates/deletes a Question object via PUT, DELETE """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (IsAdminUser,)


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs["q_pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateAnswer(APIView):
    serializer_class = AnswerSerializer
    permission_classes = (HasAnID,)

    def post(self, request, pk, q_pk):
        answered_by = AuthID.objects.get(auth_id=request.headers['auth-id']).id
        answer_text = request.data.get("answer_text")
        choice = request.data.get("choices")
        choices = request.data.get("choices")
        data = {
            'question': q_pk,
            'poll': pk,
            'answer_text': answer_text,
            'choice': choice,
            'choices': choices,
            'answered_by': answered_by,
        }
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateId(APIView):
    """ Creates an AuthID object and returns an auth_id via POST """
    serializer_class = AuthIDSerializer

    def post(self, request):
        auth_id = randint(1000000, 9999999)
        data = {'auth_id': auth_id}
        serializer = AuthIDSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data['auth_id'], status=status.HTTP_201_CREATED)
            except IntegrityError:
                return post(self, request)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
