from django.shortcuts import render
from AnswerQuest.models import Question

# These can be subject to change but these were just names I came up with.
# Remember changing names here means you have to change them in the urls.py as well


def question(request):
    # TODO
    # 1. Make question adder link to Nav page
    # 2. Make answer button that is a JavaScript added form field that when submitted is tied and added to the Question object in the model
    pass


def home_page(request):
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/home_page.html', {'questions': questions})


def user_profile(request):
    pass
