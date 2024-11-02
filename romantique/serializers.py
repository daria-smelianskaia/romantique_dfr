from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Idea, Question


class UserSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'idea']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
