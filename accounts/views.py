from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from accounts.decorators import login_required
from accounts.forms import LogInForm, SignUpForm

def signup(request):
    if request.user.is_authenticated:
        # Redirect the user to a suitable page if they are already authenticated
        return redirect('myapp:index')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('myapp:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def login_view(request):
    if request.user.is_authenticated:
        # user is already logged in, redirect to a suitable page
        return redirect('myapp:index')

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('myapp:index')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('myapp:index')


def cancel_url(request):
    return redirect('myapp:index')