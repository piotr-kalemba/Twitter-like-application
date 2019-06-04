from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin


class Tweet(models.Model):

    content = models.TextField(max_length=140)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.content if len(self.content) <= 30 else self.content[:30] + '...'

class TweetAdmin(ModelAdmin):

    def content_display(self, obj):

        return str(obj)
    def user_display(self, obj):

         return obj.user.email

    list_display = ('content_display', 'user_display')

class TweetComment(models.Model):

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=60)

    def __str__(self):

        content_part = self.content if len(self.content) <= 30 else self.content[:30] + '...'
        author_part = str(self.author)
        return author_part + ":" + content_part

class TweetCommentAdmin(ModelAdmin):

    def content_display(self, obj):

        return obj.content if len(obj.content) <= 30 else obj.content[:30] + '...'
    def author_display(self, obj):

         return obj.author.email

    list_display = ('content_display', 'author_display')


class Message(models.Model):

    content = models.TextField()
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    is_read = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.content if len(self.content) <= 30 else self.content[:30] + '...'


class MessageAdmin(ModelAdmin):

    def content_display(self, obj):
        return str(obj)

    def message_to_display(self, obj):
        return obj.message_to.email

    def message_from_display(self, obj):
        return obj.message_from.email

    def is_read_display(self, obj):
        return str(obj.is_read)

    list_display = ('content_display', 'message_to_display', 'message_from_display', 'is_read_display')