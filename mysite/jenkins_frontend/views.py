from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'jenkins_frontend/home.html')


def list(request):
    return render(request, 'jenkins_frontend/basic.html', {'content': ['List', 'list']})


def add(request):
    return render(request, 'jenkins_frontend/basic.html', {'content': ['Add', 'add']})
