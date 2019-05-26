from django import forms
from .models import Tweet, TweetComment
from django.core.validators import EmailValidator, URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import ModelForm

def validate_fresh_email(email):

    if User.objects.filter(email=email).exists():

        raise ValidationError('Email jest już zajęty')

class TweetForm(ModelForm):

    class Meta:

        model = Tweet

        fields = ['content']

class UserForm(ModelForm):

    class Meta:

        model = User

        fields = ['email', 'password']

class NewUserForm(forms.Form):

    email = forms.CharField(label='Email', widget=forms.EmailInput, validators=[validate_fresh_email])

    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

class TweetCommentForm(ModelForm):

    class Meta:

        model = TweetComment

        fields = ['content']




