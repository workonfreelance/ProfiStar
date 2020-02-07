from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, CommentForm
from .models import *
from django.contrib.auth import authenticate, login, logout

def start(request):
    # user = request.user
    # if user.is_authenticated():

    # jobs = Job.objects.all()
    # commnet_form = CommentForm( initial={'comment':"treetrt"})
    login_form = LoginForm()
    return render(request, 'main_form.html',{"login_form":login_form})

def login_out(request):
    logout(request)
    return redirect('employ:start')


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return HttpResponse("Вышло")
        else:
            return HttpResponse("Не вышло")
    else:
        user_form = UserRegistrationForm()
        return render(request, 'old/register.html', {'user_form': user_form})

def loginHTML(request):
    user_form = LoginForm()
    return render(request, f'old/login.html', {'user_form': user_form})

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
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')

def login_or(request):
    user = request.user
    comments = Comment.objects.filter(user = user)
    commnet_form = CommentForm( initial={'comment':"treetrt"})
    return render(request, 'old/login_or.html',{"comments":comments,"commnet_form":commnet_form})

def add_comment(request):
    user = request.user
    comment = request.POST["comment"]
    Comment.objects.create(user=user,comment = comment)
    return HttpResponse("Вышло")






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