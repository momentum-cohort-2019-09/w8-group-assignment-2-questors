# Generated by Django 2.2.6 on 2019-10-29 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerQuest', '0003_auto_20191029_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quests', to=settings.AUTH_USER_MODEL),
        ),
    ]