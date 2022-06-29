from django.conf.urls import url
from django.urls import path, include
from .views import (
    ExerciseListApiView,
    ExerciseDetailApiView,
    AnswerDetailApiView,
    ExerciseDetailListApiView
)

urlpatterns = [
    path('exercises/', ExerciseListApiView.as_view()),
    path('exercises/<int:pk>/', ExerciseDetailApiView.as_view()),
    path('answer/', AnswerDetailApiView.as_view()),
    path('exercises_list/<int:pk>/', ExerciseDetailListApiView.as_view()),

]
