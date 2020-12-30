from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz
from .forms import ResetPasswordForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


def index(request):
    context = {
        'heading': 'Home',
        'title': 'Home Page',
    }
    return render(request, 'index.html', context)


def start(request):
    questions = Quiz.objects.all()

    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'heading': 'Quiz',
        'title': 'Quiz-App',
        'page_obj': page_obj,
    }
    return render(request, 'start.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # get username from input field
            messages.success(request, f"Account created!!! Login as {username}")
            return redirect('login')
        # else:
        #     for msg in form.error_messages:
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form, 'heading': 'Register', 'title': 'Signup Form'})


@login_required
def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("index")


def login_req(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged-in as {username}")
            return redirect('index')
        else:
            messages.info(request, "Username / password incorrect")
            return redirect('login')
    context = {
        'heading': 'Log-in',
        'title': 'Login-Form',
        'form': form,
    }
    return render(request, 'login.html', context)


def reset_password(request):
    # top_level_domains = ['.org', '.com', '.net', '.io', '.co', '.in', '.me', '.test', '.edu', '.info', '.gov']
    # flag_mail = True
    user_object = get_user_model()
    users = user_object.objects.all()
    form = ResetPasswordForm(request.POST)
    context = {
        'title': 'ResetPassword',
        'heading': 'Forgot Password',
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            flag_user = True
            username = str(form.cleaned_data.get('username'))
            emailid = str(form.cleaned_data.get('emailid'))
            # for domain in top_level_domains:
            #     if not emailid.endswith(domain):
            #         print("&"*100)
            #         flag_mail = True
            #     else:
            #         flag_mail = False
            # if not flag_mail:
            #     print("!"*100)
            #     messages.warning(request, 'Email ID not Proper')
            #     return redirect('login')

            for user in users:
                if username == str(user):
                    messages.success(request, f' RESET Password Instructions Sent to {emailid}')
                    return redirect('login')
                else:
                    flag_user = False
            if not flag_user:
                messages.warning(request, f'Username {username} is not valid!')
                return render(request, 'reset_password.html', context)

    form = ResetPasswordForm()
    context['form'] = form
    return render(request, 'reset_password.html', context)
