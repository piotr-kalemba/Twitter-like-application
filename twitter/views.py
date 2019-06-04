from django.shortcuts import render, redirect
from django.views import View
from .models import Tweet, TweetComment, Message
from .forms import TweetForm, UserForm, TweetCommentForm, MessageForm, LoginForm, EditUserPasswordForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

class TweetList(LoginRequiredMixin, View):

    def get(self, request):
        tweets = Tweet.objects.all().order_by('-creation_date')
        form = TweetForm()
        return render(request, 'twitter/front_page.html', {'tweets': tweets, 'form': form})

    def post(self, request):

        tweet = Tweet.objects.create(content='', user=request.user)
        form = TweetForm(request.POST, instance=tweet)

        if form.is_valid():

            form.save()
            return redirect('tweet-list')


class LoginUser(View):

    def get(self, request):
        form = LoginForm()

        return render(request, 'twitter/user_form.html', {'form': form})

    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user is not None:

                login(request, user)
                return redirect('tweet-list')

            else:

                return render(request, 'twitter/user_form_error.html', {'form': form})


class CreateUser(View):

    def get(self, request):

        form = UserForm()
        return render(request, 'twitter/new_user.html', {'form': form})

    def post(self, request):

        form = UserForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(email=email, password=password, username=email)
            user.save()
            login(request, user)
            return redirect('tweet-list')

        else:
            return render(request, 'twitter/new_user.html', {'form': form})

class ChangeUserPassword(LoginRequiredMixin, View):

    def get(self, request):
        form = EditUserPasswordForm()
        return render(request, 'twitter/change_password.html', {'form': form})

    def post(self, request):

        form = EditUserPasswordForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data['password1']
            user = request.user
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('tweet-list')

        else:
            return render(request, 'twitter/change_password.html', {'form': form})


class UserView(LoginRequiredMixin, View):

    def get(self, request, pk):

        form = MessageForm()
        user = User.objects.get(pk=pk)
        tweets = list(Tweet.objects.filter(user=user))
        results = [(tweet, len(list(TweetComment.objects.filter(tweet=tweet)))) for tweet in tweets]

        return render(request, 'twitter/user_view.html', {'results': results, 'form': form, 'target_user' : user})

    def post(self, request, pk):

        form = MessageForm(request.POST)

        if form.is_valid():

            user = User.objects.get(pk=pk)
            content = form.cleaned_data['content']
            message = Message(content=content, message_to=user, message_from=request.user)
            message.save()

        return redirect('user-view', pk=pk)


class TweetView(LoginRequiredMixin, View):

    def get(self, request, tweet_pk):

        tweet = Tweet.objects.get(pk=tweet_pk)
        comments = list(TweetComment.objects.filter(tweet=tweet))
        form = TweetCommentForm()

        return render(request, 'twitter/tweet_view.html', {'tweet': tweet, 'comments': comments, 'form': form})

    def post(self, request, tweet_pk):

        tweet = Tweet.objects.get(pk=tweet_pk)
        form = TweetCommentForm(request.POST)
        comments = list(TweetComment.objects.filter(tweet=tweet))

        if form.is_valid():

            comment = TweetComment(tweet=tweet, content=form.cleaned_data['content'], author=request.user)
            comment.save()
            comments = list(TweetComment.objects.filter(tweet=tweet))
            new_form = TweetCommentForm()

            return render(request, 'twitter/tweet_view.html', {'tweet': tweet, 'comments': comments, 'form': new_form})

        else:

            return render(request, 'twitter/tweet_view.html', {'tweet': tweet, 'comments': comments, 'form': form})


class UserMessages(LoginRequiredMixin, View):

    def get(self, request):

        user = request.user
        read_messages = user.received_messages.filter(is_read=True)
        unread_messages = user.received_messages.filter(is_read=False)
        return render(request, 'twitter/user_messages.html', {'read_messages': list(read_messages), 'unread_messages': list(unread_messages)})

class ReadMessage(LoginRequiredMixin, View):

    def get(self, request, pk):

        message = Message.objects.get(pk=pk)
        if message.is_read == False and message.message_to == request.user:
            message.is_read = True
            message.save()
        return render(request, 'twitter/read_message.html', {'message': message})







