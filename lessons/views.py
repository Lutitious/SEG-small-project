from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import MusicStudentUser, Lesson, Request, Enrolment
from lessons.forms import LogInForm, SignUpForm, RequestBookingForm
from django.contrib import messages
from django.shortcuts import render


def index(request):
    return render(request, 'main.html', context={"name": 'index.html'})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('logged_in')
        else:
            messages.add_message(request, messages.ERROR, 'sign up failed')
    else:
        form = SignUpForm()
    return render(request, 'main.html', context={"name": 'sign_up.html', 'form': form})


def logged_in(request):
    # Specify which lessons are available to the user using enrolments
    lesson_list = []
    for enrolment in Enrolment.objects.filter(student__username=request.user.username).all():
        lesson_list.append(
            'Lesson: ' + enrolment.lesson.__str__() + ' - Teacher: ' + enrolment.lesson.teacher.__str__() + ' - Date: ' + enrolment.lesson.date.__str__() + ' - Time: ' + enrolment.lesson.time.__str__() + ' - Duration: ' + enrolment.lesson.duration.__str__() + ' - Price: $' + enrolment.lesson.price.__str__())
    print(lesson_list)
    return render(request, 'main.html', context={"name": 'logged_in.html', 'lesson_list': lesson_list})


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('logged_in')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
    form = LogInForm()
    return render(request, 'main.html', context={"name": 'log_in.html', 'form': form})


def log_out(request):
    logout(request)
    return redirect('index')


def request_booking(request):
    form = RequestBookingForm(request.POST)
    if form.is_valid():
        Request = form.save(commit=False)
        Request.student = request.user
        Request.save()
        return render(request, 'main.html', context={"name": 'booking_confirmation.html','lesson': request, 'student': request.user})
    else:
        form = RequestBookingForm()
    return render(request, 'main.html', context={"name": 'request_booking.html', 'form': form})
