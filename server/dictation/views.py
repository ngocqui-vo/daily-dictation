from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import DictationSerializer, LessonSerializer, TopicSerializer
from .models import Lesson, Topic, Dictation


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


