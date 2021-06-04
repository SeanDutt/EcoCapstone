from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime


class Checkin(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  item = models.CharField(max_length=150)
  servings = models.IntegerField()
  date = models.DateTimeField(default=datetime.datetime.now)