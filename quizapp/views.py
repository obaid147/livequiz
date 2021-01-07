from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Quiz, Tasks
from .forms import SignupForm, TasksForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):   # home page
    tasks = Tasks.objects.all()  # get all tasks
    form = TasksForm()
    if request.method == "POST":  # on click Add
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'New Task:- ({task}) Added.')
        return redirect("/")
    context = {
        'form': form,
        'tasks': tasks,
        'title': 'Home Page',
        'heading': 'QuizApp',
    }
    return render(request, 'index.html', context)


def update_task(request, pk):   # update tasks for superuser
    task = Tasks.objects.get(id=pk)
    form = TasksForm(instance=task)  # has instance of the task clicked

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save()
            messages.success(request, f'Task ({updated_task}) updated.')
        return redirect("/")
    context = {
        'form': form,
        'title': 'Update Task',
        'heading': 'Update Task',
    }
    return render(request, 'update_task.html', context)


def delete_task(request, pk):   # update tasks for superuser
    item = Tasks.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        messages.info(request, f"{item} Deleted!")
        return redirect('/')
    context = {
        'item': item,
        'title': 'Delete Task',
        'heading': 'Delete Task',
    }
    return render(request, 'delete_task.html', context)


def start(request):   # Quiz
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


@user_passes_test(lambda user: not user.username, login_url='/')  # if user is already logged-in
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # get username from input field
            messages.success(request, f"Account created!!! Login as {username}")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form, 'heading': 'Register', 'title': 'Signup Form'})


"""
    if a user is logged-out redirect him to index page and not reset password pages.
"""


@user_passes_test(lambda user: user.username, login_url='/')
@login_required
def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("index")


@user_passes_test(lambda user: not user.username, login_url='/')  # if user is already logged-in
def login_req(request):
    # if request.user.is_authenticated:
    #     messages.warning(request, f"You are already logged in as {request.user}")
    #     return redirect('/')
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged-in as {username}")
            return redirect('index')
        else:
            # form.errors form template
            pass
    context = {
        'heading': 'Log-in',
        'title': 'Login-Form',
        'form': form,
    }
    return render(request, 'login.html', context)
