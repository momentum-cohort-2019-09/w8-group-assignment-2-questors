from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    email = models.EmailField()
    questions = models.ForeignKey(
        to='Question', null=True, blank=True, on_delete=models.SET_NULL, related_name='questors')
    answers = models.ForeignKey(
        to='Answer', null=True, blank=True, on_delete=models.SET_NULL, related_query_name='respondors')

    # TODO create a form to collect usernames and passwords
    username = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    # TODO figure out starred

    # TODO figure out how to make this one is_correct specific?
    # solutions = models.ManyToManyField(to='Answer', blank=True, related_query_name='solvors')
    def __str__(self):
        return self.username


class Question(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=False, null=True, related_name='quests')
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    answers = models.ForeignKey(
        to='Answer', null=True, blank=True, on_delete=models.SET_NULL, related_query_name='quests')
    post_date = models.DateField(default=timezone.now)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, blank=True, null=True, related_name='responses')
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True, related_name='responses')
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body
