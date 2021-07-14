from django import forms
from .models import *
from django.core.files.images import get_image_dimensions
from django.forms import ModelForm

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class EditProfileForm(ModelForm):

  class Meta:

    model = Profile
    continent = forms.ChoiceField(choices=CONTINENTS)
    income = forms.ChoiceField(choices=INCOME_LEVELS)
    fields = ('zipCode', 'continent', 'income', 'profile_pic')

