from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('checkin/', views.checkin, name = 'checkin'),
    path('profile/', views.profile, name = 'profile'),
]