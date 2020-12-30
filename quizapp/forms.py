from django import forms
from . models import ResetPassword


class ResetPasswordForm(forms.ModelForm):
    class Meta:
        model = ResetPassword
        fields = ('username', 'emailid')
