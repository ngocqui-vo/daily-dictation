from .models import Topic, Lesson, Dictation
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'level']


class DictationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictation
        fields = ['id', 'audio_file', 'transcript']


class LessonSerializer(serializers.ModelSerializer):
    dictations = DictationSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'dictations']