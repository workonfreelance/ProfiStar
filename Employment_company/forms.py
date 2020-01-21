from django import forms
from django.forms import ModelForm
from .models import Form

class LoginForm(ModelForm):
    class Meta:
        model = Form
        fields = ['login', 'Email', 'file']