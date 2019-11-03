from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from AnswerQuest.models import User, Question, Answer
from AnswerQuest.forms import ProfileForm, QuestionForm, AnswerForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import bleach
from bleach_whitelist import print_tags, print_attrs, all_styles


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


@login_required
@csrf_exempt
@require_POST
def toggle_question_starred(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question in request.user.starred_questions.all():
        request.user.starred_questions.remove(question)
    else:
        request.user.starred_questions.add(question)
    return JsonResponse({'ok': True})


@login_required
@csrf_exempt
@require_POST
def toggle_answer_starred(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if answer in request.user.starred_answers.all():
        request.user.starred_answers.remove(answer)
    else:
        request.user.starred_answers.add(answer)
    return JsonResponse({'ok': True})


@login_required
@csrf_exempt
@require_POST
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect(to='home')


@login_required
@csrf_exempt
@require_POST
def mark_answer_correct(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    question = answer.question
    answer.is_correct = True
    answer.question.is_solved = True
    answer.save()
    answer.question.save()
    JsonResponse({'ok': True})
    return redirect(to='question', pk=question.pk)


@login_required
def pose_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.body = bleach.clean(question.body)
            question.save()
            return redirect(to='question', pk=question.pk)
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

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(instance=request.user,
                           data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='profile')
    else:
        form = ProfileForm(instance=request.user)
    # profile = request.user.pk
    # return render(request, 'AnswerQuest/profile.html', {"profile": profile})
    # user = request.user
    # return render(request, 'AnswerQuest/profile.html', {"user": user})
    return render(request, 'AnswerQuest/profile.html', {"form": form})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'AnswerQuest/question_list.html', {'questions': questions})
