# Generated by Django 4.2.5 on 2023-09-21 09:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('users', models.ManyToManyField(blank=True, help_text='Users who are connected to the chat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]