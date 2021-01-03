from django.shortcuts import render
from .models import AdvancedQuiz
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def adv_view(request):
    questions = AdvancedQuiz.objects.all()

    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'heading': 'Advanced Quiz',
        'title': 'Quiz-App',
        'page_obj': page_obj,
    }
    return render(request, 'advanced.html', context)
