from django import forms
from .models import *
from django.forms import ModelForm
from cloudinary import *

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']
    # fields = ('zipCode', 'continent', 'income', 'profile_pic')