from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add/done/$', views.added, name='added'),
    url(r'^list/$',
        ListView.as_view(queryset=Post.objects.all().order_by("-name"), template_name="django_app/list.html")),
    url(r'^list/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="django_app/post.html"))
]
