from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile


@login_required
def user_profile(request):
    images = Profile.objects.all()
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, "Your Profile was updated!")
            return render(request, 'index.html')
        else:
            messages.error(request, "Error")
            return render(request, "index.html")

    context = {'title': 'Profile', 'heading': 'User Profile', 'form': form, 'images': images}
    return render(request, 'profile.html', context)
