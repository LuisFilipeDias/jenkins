from django import forms
from django.forms import EmailInput, TextInput


class NameForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=100, widget=TextInput)
    email = forms.CharField(min_length=1, max_length=100, widget=EmailInput)