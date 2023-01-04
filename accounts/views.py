from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from accounts.decorators import authenticated_user_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('myapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@authenticated_user_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp:index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('myapp:index')
