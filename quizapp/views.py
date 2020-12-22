from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz
from django.contrib.auth.forms import UserCreationForm


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
			form.save()
			return redirect('start')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


