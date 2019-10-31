from django.shortcuts import render
from django.shortcuts import redirect
from AnswerQuest.models import User, Question, Answer
from AnswerQuest.forms import ProfileForm, QuestionForm, AnswerForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

# These can be subject to change but these were just names I came up with.
# Remember changing names here means you have to change them in the urls.py as well


def question(request, pk):
    # TODO
    # 1. Make question adder link to Nav page
    # 2. Make answer button that is a JavaScript added form field that when submitted is tied and added to the Question object in the model
    """
    Parses the specific question clicked on to the page. 
    """
    # Have the user by the question.author
    question = Question.objects.get(pk=pk)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save()
            send_mail('Your Question got an Answer!', 'Go check it out: ',
                      EMAIL_HOST_USER, [question.author.email], fail_silently=False)
            return redirect(to='question', pk=pk)
    else:
        answer_form = AnswerForm()
    return render(request, 'AnswerQuest/question.html', {'question': question})

# @login_required


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


def user_profile(request):
    pass


def profile(request):
    profile = request.user.pk
    return render(request, 'AnswerQuest/profile.html', {"profile": profile})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/question_list.html', {'questions': questions})
