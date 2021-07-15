from django import forms
from .models import *
from django.forms import ModelForm
from cloudinary import *

CONTINENTS = (
    ('Asia','Asia'),
    ('Africa', 'Africa'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('South America','South America'),
    ('Australia/Oceania','Australia/Oceania'),
    ('Antarctica','Antarctica'),
)

INCOME_LEVELS = (
    ('0 to 10k','0 to 10k'),
    ('10k to 20k', '10k to 20k'),
    ('20k to 40k','20k to 40k'),
    ('40k to 60k','40k to 60k'),
    ('60k to 80k','60k to 80k'),
    ('80k to 100k','80k to 100k'),
    ('Over 150k','Over 150k'),
)

class ProfileForm(ModelForm):
  zip = forms.CharField(label='Zip code', max_length=10)
  continent = forms.ChoiceField(choices=CONTINENTS)
  income = forms.ChoiceField(choices=INCOME_LEVELS)
  pic = forms.ImageField()