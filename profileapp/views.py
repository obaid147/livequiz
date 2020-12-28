from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .forms import ProfileForm


@login_required
def user_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile was updated!")
            return redirect('index')
        else:
            messages.error(request, "Error")
            return render(request, "index.html")
    context = {'title': 'Profile', 'heading': 'User Profile', 'form': form}
    return render(request, 'profile.html', context)
