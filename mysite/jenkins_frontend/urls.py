from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.list, name='add'),
    url(r'^list/$',
        ListView.as_view(queryset=Post.objects.all().order_by("-added")[:25], template_name="jenkins_frontend/list.html")),
    url(r'^list/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="jenkins_frontend/post.html"))
]
