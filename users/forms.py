from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={"class": "form-control py-4",
                                                             "placeholder": "Введите имя пользователя", }))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "form-control py-4",
                                                                 "placeholder": "Введите пароль", }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
