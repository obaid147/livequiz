from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Quiz


def index(request):
	questions = Quiz.objects.all()

	paginator = Paginator(questions, 1)  # Show 25 contacts per page.
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
