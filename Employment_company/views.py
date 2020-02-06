from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from .models import *
from django.contrib.auth import authenticate, login, logout

def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            # ShoppingBasket.objects.create(user=new_user)
            return HttpResponse("Вышло")
        else:
            return HttpResponse("Не вышло")
    else:
        user_form = UserRegistrationForm()
        return render(request,'register.html',{'user_form': user_form})

def loginHTML(request):
    user_form = LoginForm()
    return render(request, f'login.html',{'user_form': user_form})

def user_login(request):
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
    return render(request, 'old/login_or.html')

def login_out(request):
    logout(request)
    return HttpResponse("вышли")

# Create your views here.
# def vity_html(request, html_name):
#     return render(request, f'{html_name}.html')
#
# def index(request):
#     form = LoginForm()
#     return render(request, f'testing_forms.html', {"form": form})
#
#
# def start(request):
#     tags = Tag.objects.all()
#     jobs = Job.objects.all()
#     return render(request, f'old/start.html', {"jobs": jobs, "tags": tags})
#
#
# def deteil(request, link):
#     # job = Job.objects.get(link=link)
#     # job = get_object_or_404(Job, link=link)
#     try:
#         job = Job.objects.get(link=link)
#         return render(request, f'old/deteil.html', {"job": job})
#     except Job.DoesNotExist:
#         return render(request, f'error.html')
#
#
# def save_form(request):
#     print(request.FILES)
#     print(request.POST)
#
#     form = LoginForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#     return JsonResponse({"test": "test"})
#
#
# def user_login(request):
#     print(request.POST)
#     form = LoginForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         user = authenticate(request,
#                             username=cd['username'],
#                             password=cd['password'])
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # return JsonResponse({"test": "test"})
#                 return HttpResponse('Authenticated successfully')
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#

# # def handle_uploaded_file(f):
# #     with open('some/file/name.txt', 'wb+') as destination:
# #         for chunk in f.chunks():
# #             destination.write(chunk)
#
# def login_out(request):
#     logout(request)
#     return HttpResponse("вышли")