from django.shortcuts import render
from lessons.forms import LogInForm


# Create your views here.

def index(request):
    return render(request, 'index.html')
def log_in(request):
    form = LogInForm()
    return render(request, 'log_in.html', { 'form': form }) 