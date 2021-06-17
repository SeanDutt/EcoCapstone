from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.db.models.deletion import PROTECT

# CONTINENTS = (
#     ('Asia','Asia'),
#     ('Africa', 'Africa'),
#     ('Europe','Europe'),
#     ('North America','North America'),
#     ('South America','South America'),
#     ('Australia/Oceania','Australia/Oceania'),
#     ('Antarctica','Antarctica'),
# )

class Checkin(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  date = models.DateField(default=datetime.date.today)
  score = models.FloatField()

class Serving(models.Model):
  container = models.ForeignKey(Checkin, on_delete=PROTECT)
  key = models.CharField(max_length=100)
  value = models.IntegerField()

class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  zipCode = models.CharField(max_length=10, null=True, blank=True)
  continent = models.CharField(max_length=20, null=True, blank=True)
  income = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return str(self.user)