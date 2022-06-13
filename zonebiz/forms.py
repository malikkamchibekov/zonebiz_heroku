from django import forms
from .models import Service
from django.contrib.auth.forms import AuthenticationForm


class ServiceForm(forms.ModelForm):

    class Meta:

        model = Service

        fields = [
            'name',
            'description',
            'image',
            'price',
        ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
