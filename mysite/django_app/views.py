from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .models import Post


# Create your views here.

def index(request):
    return render(request, 'django_app/home.html')


def list(request):
    return render(request, 'django_app/basic.html', )


def add(request):
    form = NameForm()
    return render(request, 'django_app/forms.html', {'form': form})


def added(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            Post.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'])
            return render(request, 'django_app/done.html', )
        else:
            return render(request, 'django_app/invalid.html')

