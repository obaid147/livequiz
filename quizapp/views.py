from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz


def index(request):
    questions = Quiz.objects.all()

    paginator = Paginator(questions, 1)  # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'heading': 'Quiz',
        'title': 'Quiz-App',
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)


def start(request):
    context = {
        'heading': 'Home',
        'title': 'Home Page',
    }

    return render(request, 'start.html', context)


def login(request):
    users = User.objects.all()
    contents = {
        'title': 'Login',
        'heading': 'Login',
        'users': users
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('download')
        else:
            messages.info(request, 'Invalid\nUsername or Password')
            return redirect('login')
    else:
        return render(request, 'login.html', contents)
