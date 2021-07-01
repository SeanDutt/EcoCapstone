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

class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  zipCode = models.CharField(max_length=10, null=True, blank=True, default="12345")
  continent = models.CharField(max_length=20, null=True, blank=True, default="Asia")
  income = models.CharField(max_length=25, null=True, blank=True, default="0 to 10k")
  profile_pic = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

  def __str__(self):
    return str(self.user)

class Checkin(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  date = models.DateField(default=datetime.date.today)
  score = models.FloatField()

  def __str__(self):
    return str(self.profile) + ", " + str(self.date)

class Serving(models.Model):
  container = models.ForeignKey(Checkin, on_delete=PROTECT)
  key = models.CharField(max_length=100)
  value = models.IntegerField()