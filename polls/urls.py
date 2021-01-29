from django.urls import path
from .views import PollList, PollDetail, QuestionList, QuestionDetail, ChoiceList, CreateVote


app_name = 'polls'

urlpatterns = [
    path('polls/', PollList.as_view(), name="polls_list"),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/questions/', QuestionList.as_view(), name="questions_list"),
    path('polls/<int:pk>/questions/<int:q_pk>/', QuestionDetail.as_view(), name='questions_detail'),
    path('polls/<int:pk>/questions/<int:q_pk>/choices/', ChoiceList.as_view(), name='choices_list'),
    path('polls/<int:pk>/questions/<int:q_pk>/choices/<int:c_pk>/vote/', CreateVote.as_view(), name='create_vote')
]