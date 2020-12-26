from django.shortcuts import render
from .models import IntermediateQuiz
from django.core.paginator import Paginator


def inter_view(request):
    questions = IntermediateQuiz.objects.all()

    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'heading': 'Intermediate',
        'title': 'Quiz-App',
        'page_obj': page_obj,
    }
    return render(request, 'intermediate.html', context)