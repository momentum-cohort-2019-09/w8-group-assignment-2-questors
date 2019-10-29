from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    email = models.EmailField()
    questions = models.ManyToManyField(to='Question', blank=True, related_name='questors')
    answers = models.ManyToManyField(to='Answer', blank=True, related_query_name='respondors')

    # TODO create a form to collect usernames and passwords

    # TODO figure out starred

    # TODO figure out how to make this one is_correct specific?
    # solutions = models.ManyToManyField(to='Answer', blank=True, related_query_name='solvors')

class Question(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True, related_name='quests')
    title = models.CharField(max_length=100)
    body = models.TextField()
    answers = models.ManyToManyField(to='Answer', blank=True, related_query_name='quests')
    # post_date = models.DateField()
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='responses')
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True,related_name='responses')
    body = models.TextField()
    # post_date = models.DateField()
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    is_correct = models.BooleanField(default=False)


    