from django.contrib import admin

from twitter.models import Tweet, TweetComment, Message, TweetAdmin, TweetCommentAdmin, MessageAdmin

admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetComment, TweetCommentAdmin)
admin.site.register(Message, MessageAdmin)