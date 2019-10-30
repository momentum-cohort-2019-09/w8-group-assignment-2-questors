from django.shortcuts import render
from AnswerQuest.models import User, Question, Answer
from AnswerQuest.forms import ProfileForm, QuestionForm, AnswerForm

# These can be subject to change but these were just names I came up with.
# Remember changing names here means you have to change them in the urls.py as well


def question(request, pk):
    # TODO
    # 1. Make question adder link to Nav page
    # 2. Make answer button that is a JavaScript added form field that when submitted is tied and added to the Question object in the model
    """
    Parses the specific question clicked on to the page. 
    """
    question = Question.objects.get(pk=pk)
    return render(request, 'AnswerQuest/question.html', {'question': question})

# @login_required


def pose_question(request):
    if request.method == 'POST':
        form = QuestionForm(instance=request.user, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect(to='question')
    else:
        form = QuestionForm(instance=request.user)

    return render(request, 'AnswerQuest/pose_question.html', {"form": form})


def home(request):
    """
    Brings all of the questions to the homepage
    """
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/home.html', {'questions': questions})


def user_profile(request):
    pass


def profile(request):
  page = request.page
  return render(request, 'AnswerQuest/profile.html', {"page": page})