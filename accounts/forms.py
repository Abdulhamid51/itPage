from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['name','surname','avatar','git','telegram']