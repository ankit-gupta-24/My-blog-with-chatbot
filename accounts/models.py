from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        