from django.db import models

# Create your models here.


class Idea(models.Model):
    idea = models.TextField()

    class Meta:
        app_label = 'romantique'


class Question(models.Model):
    question = models.TextField()

    class Meta:
        app_label = 'romantique'