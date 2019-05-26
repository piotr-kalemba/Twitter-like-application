from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Tweet, TweetComment
from .forms import TweetForm, UserForm, NewUserForm, TweetCommentForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

class TweetList(LoginRequiredMixin, View):

    def get(self, request):

        tweets = Tweet.objects.all().order_by('-creation_date')

        return render(request, 'twitter/front_page.html', {'tweets': tweets})

class CreateTweet(LoginRequiredMixin, View):

    def get(self, request):

        form = TweetForm()

        return render(request, 'twitter/create_tweet.html', {'form': form})

    def post(self, request):

        tweet = Tweet.objects.create(content='', user=request.user)

        form = TweetForm(request.POST, instance=tweet)

        if form.is_valid():

            form.save()

            return redirect('tweet-list')


class LoginUser(View):

    def get(self, request):

        form = UserForm()

        return render(request, 'twitter/user_form.html', {'form': form})

    def post(self, request):

        form = UserForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            if user is not None:

                login(request, user)

                return redirect('tweet-list')

            else:

                return HttpResponse('Błędne dane logowania!')

class CreateUser(View):

    def get(self, request):

        form = NewUserForm()

        return render(request, 'twitter/new_user.html', {'form': form})

    def post(self, request):

        form = NewUserForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            user = User(email=email, password=password, username=email)

            user.save()

            login(request, user)

            return redirect('tweet-list')

        else:

            return HttpResponse('Email już zajęty!')

class UserView(LoginRequiredMixin, View):

    def get(self, request, user_pk):

        user = User.objects.get(pk=user_pk)

        tweets = list(Tweet.objects.filter(user=user))

        results = [(tweet, len(list(TweetComment.objects.filter(tweet=tweet)))) for tweet in tweets]

        return render(request, 'twitter/user_view.html', {'results': results})

class TweetView(LoginRequiredMixin, View):

    def get(self, request, tweet_pk):

        tweet = Tweet.objects.get(pk=tweet_pk)

        comments = list(TweetComment.objects.filter(tweet=tweet))

        form = TweetCommentForm()

        return render(request, 'twitter/tweet_view.html', {'tweet': tweet, 'comments': comments, 'form': form})

    def post(self, request, tweet_pk):

        tweet = Tweet.objects.get(pk=tweet_pk)

        form = TweetCommentForm(request.POST)

        if form.is_valid():

            comment = TweetComment(tweet=tweet, content=form.cleaned_data['content'])

            comment.save()

            comments = list(TweetComment.objects.filter(tweet=tweet))

            new_form = TweetCommentForm()

            return render(request, 'twitter/tweet_view.html', {'tweet': tweet, 'comments': comments, 'form': new_form})

        else:

            return HttpResponse('Błąd formularza!')







