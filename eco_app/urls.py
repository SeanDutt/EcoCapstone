from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('checkin/', views.checkinpage, name = 'checkin'),
    path('profile/', views.profilepage, name = 'profile'),
    path('add_checkin/', views.add_checkin, name = 'add_checkin'),
    path('compare/', views.compare, name = 'compare'),
    path('editProfile/', views.editProfile, name = 'editProfile'),
]