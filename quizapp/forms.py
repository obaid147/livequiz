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
            'title': forms.TextInput(attrs={'placeholder': 'Add New Task....'})
        }

    # remove label from title field
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        # super().__init__() instance is removed from update_task when used
        self.fields['title'].label = ''
