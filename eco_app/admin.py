from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Checkin)
admin.site.register(models.Serving)
admin.site.register(models.Profile)