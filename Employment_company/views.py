from django.shortcuts import render
from .forms import LoginForm
from .models import Form

# Create your views here.
def vity_html(request, html_name):
    return render(request, f'{html_name}.html')


def index(request):
    form = LoginForm()
    return render(request, f'testing_forms.html', {"form": form})


def save_form(request):
    print(request.FILES)
    print(request.POST)

    form = LoginForm(request.POST)
    if form.is_valid():
        F =  Form(request.POST,request.FILES)
        F.save()
    return render(request, f'index.html')
