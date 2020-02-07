"""ProfiStar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Employment_company.views import *

app_name = "employ"

urlpatterns = [
    path('', start, name="start"),

    path('registration', registration, name="registration"),
    path('login',loginHTML,name="login"),
    path('user_login',user_login,name="user_login"),
    path('add_comment', add_comment, name="add_comment"),

    # path('', start, name="start"),
    # path('save_form', save_form, name="save_form"),
    # # path('<str:html_name>', vity_html, name="vity_html")
    path('login_out', login_out, name="login_out"),
    path('login_or',login_or,name="login_or"),
    # path('user_login',user_login,name="user_login"),
    # path('index', index, name="index"),
    # path('deteil/<str:link>', deteil, name="deteil"),

]
