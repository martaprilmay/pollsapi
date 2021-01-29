from django.urls import path
from .views import (PollList, ActivePollsList, PollCreate, PollDetail, QuestionList, QuestionDetail, QuestionCreate,
                    ChoiceList, ChoiceCreate, CreateVote, CreateVotes, CreateAnswer)


app_name = 'polls'

urlpatterns = [
    path('polls/', ActivePollsList.as_view(), name="active_polls_list"),
    path('polls/all', PollList.as_view(), name="polls_list"),
    path('polls/create', PollCreate.as_view(), name="polls_create"),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),

    path('polls/<int:pk>/questions/', QuestionList.as_view(), name="questions_list"),
    path('polls/<int:pk>/questions/create', QuestionCreate.as_view(), name="questions_create"),
    path('polls/<int:pk>/questions/<int:q_pk>/', QuestionDetail.as_view(), name='questions_detail'),

    path('polls/<int:pk>/questions/<int:q_pk>/choices/', ChoiceList.as_view(), name='choices_list'),
    path('polls/<int:pk>/questions/<int:q_pk>/choices/create', ChoiceCreate.as_view(), name='choices_create'),

    path('polls/<int:pk>/questions/<int:q_pk>/choices/<int:c_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('polls/<int:pk>/questions/<int:q_pk>/votes', CreateVotes.as_view(), name='create_votes'),
    path('polls/<int:pk>/questions/<int:q_pk>/answer', CreateAnswer.as_view(), name='create_answer'),
]