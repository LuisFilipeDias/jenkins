from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'django_app/home.html')


def list(request):
    return render(request, 'django_app/basic.html',)


def add(request):
    return render(request, 'django_app/basic.html', {'content': ['Add', 'add']})
