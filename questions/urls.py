from django.urls import path
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, questionVoteView,
                            answerVoteView,homeFeedView, testView, leaderboardView)


urlpatterns = [
    path('', homeFeedView, name ='home'),
    path('test/', testView),
    path('leaderboard/', leaderboardView),
    path('question/<int:id>/', questionView),
    path('question/<int:id>/vote', questionVoteView),
    path('answer/<int:id>/vote', answerVoteView),
    path('question/<int:id>/answer', answerView),
    path('question/new/', newView, name ='question_create' ),
    path('question/my_answers/', myAnswersView, name='my-answers'),
    path('question/my_questions/', myQuestionsView, name='my-questions'),
]
