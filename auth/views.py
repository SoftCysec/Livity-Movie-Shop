from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:index')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('myapp:index')
