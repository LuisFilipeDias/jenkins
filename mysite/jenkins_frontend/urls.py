from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/$',
        ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="jenkins_frontend/add.html"))
]
