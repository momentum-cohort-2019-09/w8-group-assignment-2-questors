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
from django.urls import path
from AnswerQuest import views

# None of these views are set up so if you try running this, it will break
urlpatterns = [
    path('', views.home, name='home'),
    path('AnswerQuest/user_profile/<int:pk>',
         views.user_profile, name='user_profile'),
    path('AnswerQuest/pose_question', views.pose_question, name="pose_question"),
    path('AnswerQuest/question/<int:pk>', views.question, name="question"),
    path('AnswerQuest/question/question_list', views.question, name="question_list"),
    path('admin/', admin.site.urls),
]
