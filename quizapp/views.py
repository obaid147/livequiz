from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz, ResetPassword
from . forms import ResetPasswordForm
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
            user = form.save()
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
	User = get_user_model()
	users = User.objects.all()
	form = ResetPasswordForm(request.POST)
	flag = True
	if request.method == 'POST':
		if form.is_valid():
			username = str(form.cleaned_data.get('username'))
			emailid = form.cleaned_data.get('emailid')

			context = {
					'title': 'ResetPassword',
					'heading': 'Forgot Password',
					'form': form,
					}
			for user in users:
				if username == str(user):
					flag = True
					messages.success(request, f'Password Sent to {emailid}')
					return redirect('login')
				else:
					flag = False
			if not flag:
				messages.warning(request, f'Username {username} is not valid!')
				return render(request, 'reset_password.html', context)
			
	else:
		form = ResetPasswordForm()
		return render(request, 'reset_password.html', {'form':form})
