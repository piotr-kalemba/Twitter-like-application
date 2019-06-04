from django import forms
from .models import Tweet, TweetComment, Message
from django.core.validators import EmailValidator, URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

def validate_fresh_email(email):

    if User.objects.filter(email=email):
        raise ValidationError('Email jest już zajęty')

class TweetForm(ModelForm):

    class Meta:

        model = Tweet
        fields = ['content']


class UserForm(UserCreationForm):

    email = forms.EmailField(label='Email', required=True, validators=[validate_fresh_email])
    class Meta:

        model = User
        fields = ['email', 'password1','password2']

class LoginForm(forms.Form):

    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Hasło', required=True, widget=forms.PasswordInput)

class EditUserPasswordForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['password1', 'password2']


class TweetCommentForm(ModelForm):

    class Meta:

        model = TweetComment
        fields = ['content']

class MessageForm(ModelForm):

    class Meta:

        model = Message
        fields = ['content']






