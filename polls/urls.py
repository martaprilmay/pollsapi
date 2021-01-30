from django.urls import path
from .views import (PollList, ActivePollsList, PollCreate, PollUpdate, PollDetail,
                    QuestionList, QuestionCreate, QuestionUpdate, QuestionDetail,
                    ChoiceList, ChoiceCreate, ChoiceUpdate,
                    CreateAnswer,
                    CreateId)


app_name = 'polls'

urlpatterns = [
    path('polls/', ActivePollsList.as_view(), name="active_polls_list"),
    path('polls/all', PollList.as_view(), name="polls_list"),
    path('polls/create', PollCreate.as_view(), name="polls_create"),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/update', PollUpdate.as_view(), name='polls_update'),

    path('polls/<int:pk>/questions/', QuestionList.as_view(), name="questions_list"),
    path('polls/<int:pk>/questions/create', QuestionCreate.as_view(), name="questions_create"),
    path('polls/<int:pk>/questions/<int:q_pk>/', QuestionDetail.as_view(), name='questions_detail'),
    path('questions/<int:pk>/update', QuestionUpdate.as_view(), name='questions_update'),

    path('polls/<int:pk>/questions/<int:q_pk>/choices/', ChoiceList.as_view(), name='choices_list'),
    path('polls/<int:pk>/questions/<int:q_pk>/choices/create', ChoiceCreate.as_view(), name='choices_create'),
    path('choices/<int:pk>/update', ChoiceUpdate.as_view(), name='choices_update'),

    path('polls/<int:pk>/questions/<int:q_pk>/answer', CreateAnswer.as_view(), name='create_answer'),

    path('createid', CreateId.as_view(), name='create_id')
]
