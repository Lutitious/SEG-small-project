from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def log_in(request):
    return render(request, 'log_in.html')