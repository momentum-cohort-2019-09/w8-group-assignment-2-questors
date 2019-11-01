from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    email = models.EmailField()

    # TODO figure out starred
    starred_questions = models.ManyToManyField(
        to='Question', related_name='Qfans', blank=True)
    # starred_answer = models.ManyToManyField(
    #     to='Answer', related_name='Afans', blank=True)
    # starred = models.ForeignKey(
    #     to='Question', on_delete=models.SET_NULL, blank=True, null=True, related_name='fan')

    # TODO figure out how to make this one is_correct specific?
    # solutions = models.ManyToManyField(to='Answer', blank=True, related_query_name='solvors')
    def __str__(self):
        return self.username


class Question(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=False, null=True, related_name='quests')
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    # answers = models.ForeignKey(
    #     to='Answer', null=True, blank=True, on_delete=models.SET_NULL, related_query_name='quests')
    post_date = models.DateField(default=timezone.now)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Should we get rid of the delete?
# Argument: We should be able to in case of social issues.
class Answer(models.Model):
    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, blank=True, null=True, related_name='answers')
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True, related_name='responses')
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    # TALK ABOUT THIS AND IF THIS IS NECESSARY
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body
