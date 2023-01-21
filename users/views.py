from django.shortcuts import render, redirect
from django.contrib import auth

from .models import *
from .forms import *


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    return render(request, 'users/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def profile(request):
    return render(request, 'users/profile.html')
