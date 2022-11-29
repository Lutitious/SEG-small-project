from django.shortcuts import render
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

