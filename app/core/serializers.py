from dataclasses import field
from pkg_resources import require
from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=["alternative"]


class ExerciseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Exercise
        fields = ["description", "alternatives", "correct_alternative"]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["alternative_selected","from_exercise"]

class ExerciseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseList
        fields = ["exercises"]
