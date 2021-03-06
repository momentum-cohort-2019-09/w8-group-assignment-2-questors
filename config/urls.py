"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AnswerQuest import views
from django.conf import settings
from django.conf.urls.static import static

# None of these views are set up so if you try running this, it will break
urlpatterns = [
    path('', views.home, name='home'),
    path('AnswerQuest/user_profile/<int:pk>',
         views.user_profile, name='user_profile'),
    path('AnswerQuest/pose_question', views.pose_question, name="pose_question"),
    path('AnswerQuest/question/<int:pk>', views.question, name="question"),
    path('AnswerQuest/question/<int:pk>/starred/',
         views.toggle_question_starred, name="toggle_question_starred"),
    path('AnswerQuest/answer/<int:pk>/starred/',
         views.toggle_answer_starred, name="toggle_answer_starred"),
    path('AnswerQuest/answer/<int:pk>/correct/',
         views.mark_answer_correct, name="mark_answer_correct"),
    path('AnswerQuest/question_list', views.question_list, name="question_list"),
    path('admin/', admin.site.urls),
    path('AnswerQuest/question/<int:pk>/delete/',
         views.delete_question, name="delete_question"),
    path('AnswerQuest/profile', views.profile, name="profile"),
    path('accounts/', include('registration.backends.default.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
