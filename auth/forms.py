from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass
