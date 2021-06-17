from api.models import Impact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Checkin, Serving, Profile


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

@login_required
def profile(request):
    continent = Checkin.objects.filter()
    incomeLevel = Checkin.objects.filter()
    zipCode = Checkin.objects.filter()
    checkins = Checkin.objects.filter(user=request.user)
    context = {
        'continent':continent,
        'incomeLevel':incomeLevel,
        'zipCode':zipCode,
        'checkins':checkins
    }
    return render(request, 'pages/profile.html', context)

@login_required
def editProfile(request):
    if request.method == 'GET':
        return render(request, 'pages/editProfile.html')

    if request.method == 'POST':
        user = Profile.objects.filter(user=request.user).first()
        user.zipCode = request.POST.get("zip")
        user.continent = request.POST.get("continent")
        user.income = request.POST.get("income")
        user.save()
        return profile(request)

@login_required
def checkin(request):
    if request.method == 'GET':
        return render(request, 'pages/checkin.html')


@login_required
def add_checkin(request):
    api_list = Impact.objects.all()
    checkin = Checkin.objects.create(score=0)
    footprint = 0
    for item in api_list:
        check = request.POST.get(item.item)
        footprint += int(check) * float(item.co2PerUnit)
        Serving.objects.create(container=checkin, key=item, value=int(check))

    checkin.user = request.user
    checkin.score = footprint
    checkin.save()

    return redirect('checkin')

@login_required
def compare(request):
    away = User.objects.get(username=request.POST['compare'])
    home = Checkin.objects.filter(user=request.user).order_by('date')

    context = {
        'home':home,
        'away':away,
    }
    return render(request, 'pages/compare.html', context)
