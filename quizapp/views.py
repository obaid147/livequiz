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


def register(request):
    contents = {
        'title': 'Register',
        'heading': 'Register'
    }

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'UserName Taken')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')

            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
            )
            user.save()
            messages.success(request, 'User Created')  # <-
            return redirect('login')
        else:
            messages.error(request, 'Password Mismatch')
            return redirect('register')
    else:
        return render(request, 'app/register.html', contents)

