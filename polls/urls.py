from django.urls import path
from .views import PollList, PollDetail, QuestionList, QuestionDetail, ChoiceList, CreateVote

urlpatterns = [
    path('polls/', PollList.as_view(), name="polls_list"),
    path('polls/<int:pk>', PollDetail.as_view(), name='polls_detail'),
    path('questions/', QuestionList.as_view(), name="questions_list"),
    path('questions/<int:pk>', QuestionDetail.as_view(), name='questions_detail'),
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote', CreateVote.as_view(), name='create_vote')
]