from django.shortcuts import render

# Create your views here.
def vity_html(request, html_name):
    return render(request, f'{html_name}.html')
