from django.http import JsonResponse
from django.shortcuts import render
from .forms import LoginForm
from .models import *
from .models import Form

# Create your views here.
# def vity_html(request, html_name):
#     return render(request, f'{html_name}.html')


def index(request):
    form = LoginForm()
    return render(request, f'testing_forms.html', {"form": form})

def start(request):
    jobs = Job.objects.all()
    return render(request, f'start.html', {"jobs": jobs})


def deteil(request,link):
    job = Job.objects.get(link=link)
    return render(request, f'deteil.html', {"job": job})

def save_form(request):
    print(request.FILES)
    print(request.POST)

    form = LoginForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return JsonResponse({"test":"test"})


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)