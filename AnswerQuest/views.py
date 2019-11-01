from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from AnswerQuest.models import User, Question, Answer
from AnswerQuest.forms import ProfileForm, QuestionForm, AnswerForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

# These can be subject to change but these were just names I came up with.
# Remember changing names here means you have to change them in the urls.py as well


def question(request, pk):
    """
    Parses the specific question clicked on to the page. 
    """
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            send_mail('Your Question got an Answer!', f'Go check it out: http://127.0.0.1:8000/AnswerQuest/question/{pk}',
                      EMAIL_HOST_USER, [question.author.email], fail_silently=False)
            return redirect(to='question', pk=pk)
    else:
        form = AnswerForm(instance=request.user)

    question = Question.objects.get(pk=pk)
    return render(request, 'AnswerQuest/question.html', {'form': form, 'question': question})
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
