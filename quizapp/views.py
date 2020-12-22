from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate



def index(request):
    context = {
        'heading': 'Home',
        'title': 'Home Page',
    }
    return render(request, 'index.html', context)


def start(request):
    questions = Quiz.objects.all()

    paginator = Paginator(questions, 1)  # Show 25 contacts per page.
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
			username = form.cleaned_data.get('username')
			messages.success(request, f"You can now login as {username}")
			return redirect('signin')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


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
			messages.info(request, f"You are now loggedin as {username}")
			return redirect('index')
	context = {
        'heading': 'Signin',
        'title': 'Sign-Form',
        'form': form,
    }
	return render(request, 'login.html', context)