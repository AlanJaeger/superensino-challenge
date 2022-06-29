from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Question(models.Model):
    alternative = models.CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.alternative

class Exercise(models.Model):
    description = models.CharField(max_length=180, null=True, blank=True)
    alternatives = models.ManyToManyField(
        Question, related_name="multiple_choice", blank=True)
    correct_alternative = models.IntegerField()
    correct = models.CharField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.description

class Answer(models.Model):
    alternative_selected = models.ForeignKey(Question, on_delete=models.SET_NULL, blank=True, null=True)
    from_exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, blank=True, null=True)

class ExerciseList(models.Model):
    exercises = models.ManyToManyField(
        Exercise, related_name="exercise_list", blank=True)