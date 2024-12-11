from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import DictationSerializer, TopicSerializer, LessonDetailSerializer, LessonListSerializer
from .models import Lesson, Topic, Dictation


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':  # Khi gọi chi tiết Lesson
            return LessonDetailSerializer
        return LessonListSerializer  # Khi gọi danh sách Lesson

