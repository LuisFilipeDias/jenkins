from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'jenkins_frontend/home.html')


def list(request):
    return render(request, 'jenkins_frontend/basic.html',)


def add(request):
    return render(request, 'jenkins_frontend/basic.html', {'content': ['Add', 'add']})
