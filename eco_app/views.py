from api.models import Impact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
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
    
    if len(checkins):
        avg = round(avg / len(checkins), 2)

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
    user = User.objects.filter(username=request.POST.get("compare"))
    away = Checkin.objects.filter(profile=user.first().profile)
    home = Checkin.objects.filter(profile=request.user.profile)

    # print(away.last().date, home.last().date)
    if away[0].date <= home[0].date: # Finds the first date checked in between both users
        first = away[0].date
    else:
        first = home[0].date

    # print(first)

    if away.last().date <= home.last().date: # Finds the most recent checkin between both users
        last = home.last().date
    else:
        last = away.last().date

    # print(last)

    step = datetime.timedelta(days=1)
    timeline = []

    while first <= last:
        timeline.append(first)
        first += step

    # print(timeline)

    user_checkins = []
    compare_checkins = []

    for day in timeline:
        if Checkin.objects.filter(profile=user.first().profile, date=day):
            user_checkins.append(Checkin.objects.get(profile=user.first().profile, date=day))
        else:
            user_checkins.append(None)

        if Checkin.objects.filter(profile=request.user.profile, date=day):
            compare_checkins.append(Checkin.objects.get(profile=request.user.profile, date=day))
        else:
            compare_checkins.append(None)

    # print(user_checkins, compare_checkins)

    context = {
        'timeline':timeline,
        'user_checkins':user_checkins,
        'compare_checkins':compare_checkins,
    }
    return render(request, 'pages/compare.html', context)