from django.urls import path
from .views import (PollList, ActivePollsList, PollCreate, PollUpdate, PollDetail,
                    QuestionList, QuestionCreate, QuestionUpdate, QuestionDetail,
                    ChoiceList, ChoiceCreate, ChoiceUpdate,
                    CreateAnswer, MyAnswers,
                    CreateId)


app_name = 'polls'

urlpatterns = [
    path('polls/', ActivePollsList.as_view(), name="active-polls-list"),
    path('polls/all', PollList.as_view(), name="polls-list"),
    path('polls/create', PollCreate.as_view(), name="poll-create"),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls-detail'),
    path('polls/<int:pk>/update', PollUpdate.as_view(), name='polls-update'),

    path('polls/<int:pk>/questions/', QuestionList.as_view(), name="questions-list"),
    path('polls/<int:pk>/questions/create', QuestionCreate.as_view(), name="questions-create"),
    path('polls/<int:pk>/questions/<int:q_pk>/', QuestionDetail.as_view(), name='questions-detail'),
    path('questions/<int:pk>/update', QuestionUpdate.as_view(), name='questions-update'),

    path('polls/<int:pk>/questions/<int:q_pk>/choices/', ChoiceList.as_view(), name='choices-list'),
    path('polls/<int:pk>/questions/<int:q_pk>/choices/create', ChoiceCreate.as_view(), name='choices-create'),
    path('choices/<int:pk>/update', ChoiceUpdate.as_view(), name='choices-update'),

    path('polls/<int:pk>/questions/<int:q_pk>/answer', CreateAnswer.as_view(), name='create-answer'),
    path('polls/my-answers', MyAnswers.as_view(), name='my-answers'),

    path('create-id', CreateId.as_view(), name='create-id')
]
