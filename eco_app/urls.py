from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('checkin/', views.checkinpage, name = 'checkin'),
    path('profile/', views.profilepage, name = 'profile'),
    path('add_checkin/', views.add_checkin, name = 'add_checkin'),
    path('compare/<username>', views.compare, name = 'compare'),
    path('editProfile/', views.editProfile, name = 'editProfile'),
    path('index/', views.user_index, name = 'index'),
    path('profile/<username>', views.other_profile, name = 'other_profile'),
]