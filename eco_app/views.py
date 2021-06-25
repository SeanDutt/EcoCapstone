from api.models import Impact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
import datetime

from .models import Checkin, Serving, Profile, User


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

@login_required
def profilepage(request):
    today = datetime.date.today()
    d = today.strftime("%Y-%m-%d")

    contScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.continent == request.user.profile.continent:
                contScores.append(checkin)


    zipScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.zipCode == request.user.profile.zipCode:
                zipScores.append(checkin)


    incomeScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.income == request.user.profile.income:
                incomeScores.append(checkin)

    checkins = Checkin.objects.filter(profile=request.user.profile)
    avg = 0
    for checkin in checkins:
        avg += checkin.score
    avg = avg / len(checkins)

    context = {
        'avg':avg,
        'contScores':contScores,
        'zipScores':zipScores,
        'incomeScores':incomeScores,
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
        return profilepage(request)

@login_required
def checkinpage(request):
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

    checkin.profile = request.user.profile
    checkin.score = footprint
    checkin.save()

    return redirect('checkin')

@login_required
def compare(request):
    user = User.objects.filter(username=request.POST.get("compare")).first().id
    away = Checkin.objects.filter(profile=user) 
    home = Checkin.objects.filter(profile=request.user.profile)

    context = {
        'home':home,
        'away':away,
    }
    return render(request, 'pages/compare.html', context)