from django import forms
from .models import *
from django.forms import ModelForm

CONTINENTS = (
    ('',''),
    ('Asia','Asia'),
    ('Africa', 'Africa'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('South America','South America'),
    ('Australia/Oceania','Australia/Oceania'),
    ('Antarctica','Antarctica'),
)

INCOME_LEVELS = (
    ('',''),
    ('0 to 10k','0 to 10k'),
    ('10k to 20k', '10k to 20k'),
    ('20k to 40k','20k to 40k'),
    ('40k to 60k','40k to 60k'),
    ('60k to 80k','60k to 80k'),
    ('80k to 100k','80k to 100k'),
    ('Over 150k','Over 150k'),
)

class ProfileForm(forms.Form):
  class Meta:
    model = Profile
    exclude = ['user']