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



class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'created_at', 'updated_at']

class LessonDetailSerializer(serializers.ModelSerializer):
    dictations = DictationSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'created_at', 'updated_at', 'dictations']
