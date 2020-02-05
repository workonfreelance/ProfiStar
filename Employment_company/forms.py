from django import forms
from django.forms import ModelForm
# from .models import Form

# class LoginForm(ModelForm):
#     class Meta:
#         model = Form
#         fields = ['login', 'Email', 'file']


class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password',widget=forms.PasswordInput)



# class RegitrUserForm()