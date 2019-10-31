from django.shortcuts import render
from django.shortcuts import redirect
from AnswerQuest.models import User, Question, Answer
from AnswerQuest.forms import ProfileForm, QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

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

@login_required
def pose_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(to='/')
    else:
        form = QuestionForm(instance=request.user)

    return render(request, 'AnswerQuest/pose_question.html', {"form": form})


def home(request):
    """
    Brings all of the questions to the homepage
    """
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/home.html', {'questions': questions})

@login_required
def user_profile(request):
    pass

@login_required
def profile(request):
    # profile = request.user.pk
    # return render(request, 'AnswerQuest/profile.html', {"profile": profile})
    user = request.user
    return render(request, 'AnswerQuest/profile.html', {"user": user})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/question_list.html', {'questions': questions})
    