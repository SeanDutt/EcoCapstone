from django.contrib.auth.models import User
from eco_app.models import Checkin
from api.models import Impact
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from api.models import Impact


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def profile(request):
    return render(request, 'pages/profile.html')

def checkin(request):
    if request.method == 'GET':
        return render(request, 'pages/checkin.html')

def add_checkin(request):
    api_list = Impact.objects.all()

    for item in api_list:
        check = request.POST.get(item.item)
        # footprint = int(check) * float(item.co2PerUnit)
        user = request.user
        Checkin.objects.create(user=user, item=item, servings=int(check))

    return redirect('checkin')

