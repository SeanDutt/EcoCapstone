from django.contrib.auth import models
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eco_app.models import Profile


def user_register(request):
  if request.method == 'POST':
    new_user = User(
      username = request.POST['username'],
      email = request.POST['email'],
    )
    new_user.set_password(request.POST['password'])
    new_user.save()
    Profile.objects.create(user=new_user)
    return redirect('login')
  return render(request, 'register/register.html')

def user_login(request):
  if request.method == 'POST':
    user = authenticate(
      request,
      username = request.POST['username'],
      password = request.POST['password'],
    )

    if user is not None:
      login(request, user)
      return redirect('home')
  return render(request, 'register/login.html')

def user_logout(request):
  logout(request)
  return redirect('home')