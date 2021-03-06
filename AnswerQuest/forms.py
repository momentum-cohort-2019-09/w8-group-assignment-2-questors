from django import forms
from AnswerQuest.models import User, Question, Answer


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'avatar',
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        widgets = {
            'body': forms.Textarea(attrs={'id': 'answer_box'})
        }
        fields = [
            'body',
        ]
