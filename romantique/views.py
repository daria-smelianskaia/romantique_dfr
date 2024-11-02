from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerial, QuestionSerializer
from .models import Idea, Question
from .serializers import IdeaSerializer

import random


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerial
    permission_classes = [permissions.IsAuthenticated]


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    @action(detail=False, methods=['GET'])
    def random(self, request):
        res = random.choice([idea.idea for idea in self.queryset])
        return Response({"message": res}, status=200)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['GET'])
    def random(self, request):
        res = random.choice([q.question for q in self.queryset])
        return Response({"message": res}, status=200)


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]