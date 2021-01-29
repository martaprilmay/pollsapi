from django.contrib import admin
from .models import Poll, Question, Choice, Vote, Votes, Answer


admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Votes)
admin.site.register(Answer)
