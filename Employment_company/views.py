from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .models import *
from django.shortcuts import get_object_or_404
# from .models import Form
from django.contrib.auth import authenticate, login,logout

# Create your views here.
# def vity_html(request, html_name):
#     return render(request, f'{html_name}.html')

def index(request):
    form = LoginForm()
    return render(request, f'testing_forms.html', {"form": form})


def start(request):
    tags = Tag.objects.all()
    jobs = Job.objects.all()
    return render(request, f'start.html', {"jobs": jobs, "tags": tags})


def deteil(request, link):
    # job = Job.objects.get(link=link)
    # job = get_object_or_404(Job, link=link)
    try:
        job = Job.objects.get(link=link)
        return render(request, f'deteil.html', {"job": job})
    except Job.DoesNotExist:
        return render(request, f'error.html')


def save_form(request):
    print(request.FILES)
    print(request.POST)

    form = LoginForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return JsonResponse({"test": "test"})


def user_login(request):
    print(request.POST)
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                # return JsonResponse({"test": "test"})
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')

def login_or(request):
    return render(request, f'login_or.html')
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def login_out(request):
    logout(request)
    return HttpResponse("вышли")