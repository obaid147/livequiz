from django import forms
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class TasksForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Title'}),
        }
