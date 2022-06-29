from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from core.serializers import *
# Create your views here.

class ExerciseListApiView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        answer = Answer.objects.all()

        answer_list = list()
        for i in answer:
            question_name = i.from_exercise.description
            if question_name in serializer.data[0]['description']:
                answer_list.append(i.id)
        new_serializer_data = list(serializer.data)    
        new_serializer_data.append({'answer':answer_list})
            
        return Response(new_serializer_data, status=status.HTTP_200_OK)


class ExerciseDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return Exercise.objects.get(id=pk)
        except Exercise.DoesNotExist:
            return None

    def get(self, request, pk):

        exercise_instance = self.get_object(pk)
        if not exercise_instance:
            return Response(
                {"response": "Exercise Object with that id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExerciseSerializer(exercise_instance)
        answer = Answer.objects.all()

        answer_list = list()
        for i in answer:
            question_name = i.from_exercise.description
            if question_name in serializer.data['description']:
                answer_list.append(i.id)

        new_serializer= dict()
        new_serializer.update(serializer.data)
        new_serializer.update({"answer": answer_list})

        return Response(new_serializer, status=status.HTTP_200_OK)


class AnswerDetailApiView(APIView):

    def post(self, request):
        data = {
            'alternative_selected': request.data.get('alternative_selected'),
            'from_exercise': request.data.get('from_exercise'),
        }
        serializer = AnswerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetailListApiView(APIView):
    def get_object(self, pk):
        try:
            return ExerciseList.objects.get(id=pk)
        except ExerciseList.DoesNotExist:
            return None

    def get(self, request, pk):

        exercise_instance = self.get_object(pk)
        if not exercise_instance:
            return Response(
                {"response": "Exercise list Object with that id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExerciseListSerializer(exercise_instance)

        exercices=Exercise.objects.filter(id__in=serializer.data['exercises'])
        answers=Answer.objects.filter(from_exercise__in=exercices)

        answers_list  = list()
        correct_alternative_list = list()

        for i in answers:
            answers_list.append(i.alternative_selected.alternative)

        for i in exercices:
            correct_alternative_list.append(i.correct)

        new_serializer = dict()

        rigths = 0
        errors = 0

        for i in correct_alternative_list:
            if i in answers_list:
                rigths+=1
            else:
                errors+=1

        percentage = 100 * (rigths/len(correct_alternative_list))    
        new_serializer.update({"successes": rigths})
        new_serializer.update({"errors": errors})
        new_serializer.update({"percentage": str(percentage)+'%'})
  
        return Response(new_serializer, status=status.HTTP_200_OK)