from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Quiz
import time


def index(request):
	questions = Quiz.objects.all()

	paginator = Paginator(questions, 1)  # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'index.html', {'page_obj': page_obj})
