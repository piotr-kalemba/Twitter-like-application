from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.admin import ModelAdmin


class Tweet(models.Model):

    content = models.TextField(max_length=140)

    creation_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.content[:30]


class TweetComment(models.Model):

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    content = models.TextField(max_length=60)

    def __str__(self):

        return self.content[:30]