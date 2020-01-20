from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    email = forms.EmailField()
    file = forms.FileField()