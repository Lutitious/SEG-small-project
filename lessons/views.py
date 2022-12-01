from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LogInForm
from lessons.forms import LogInForm

from django.shortcuts import render
from .forms import SignUpForm


def index(request):
    return render(request, 'index.html')
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('logged_in')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})



def logged_in(request):
    return render(request, 'logged_in.html')


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('logged_in')
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})
