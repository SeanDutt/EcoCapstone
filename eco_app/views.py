from django.db.models.query import EmptyQuerySet
from api.models import Impact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django import forms
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Checkin, Serving, Profile, User
from cloudinary import *

def home(request):
    return render(request, 'pages/home.html')


@login_required
def profilepage(request):
    today = datetime.date.today()
    d = today.strftime("%Y-%m-%d")

    users = User.objects.all()

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

    avg = 0
    checkins = Checkin.objects.filter(profile=request.user.profile)

    for checkin in checkins:
        avg += checkin.score

    if len(checkins):
        avg = round(avg / len(checkins), 2)

    context = {
        'avg': avg,
        'contScores': contScores,
        'zipScores': zipScores,
        'incomeScores': incomeScores,
        'checkins': checkins,
        'users': users,
    }
    return render(request, 'pages/profile.html', context)


@login_required
def other_profile(request, username):
    user = User.objects.get(username=username)

    today = datetime.date.today()
    d = today.strftime("%Y-%m-%d")

    contScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.continent == user.profile.continent:
                contScores.append(checkin)

    zipScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.zipCode == user.profile.zipCode:
                zipScores.append(checkin)

    incomeScores = []
    for checkin in Checkin.objects.all():
        if str(checkin.date) == d:
            if checkin.profile.income == user.profile.income:
                incomeScores.append(checkin)

    checkins = Checkin.objects.filter(profile=user.profile)
    avg = 0
    for checkin in checkins:
        avg += checkin.score

    if len(checkins):
        avg = round(avg / len(checkins), 2)

    context = {
        'user': user,
        'avg': avg,
        'contScores': contScores,
        'zipScores': zipScores,
        'incomeScores': incomeScores,
        'checkins': checkins
    }
    return render(request, 'pages/other_profile.html', context)


@login_required
def compare(request, username):
    user = User.objects.get(username=username)
    away = Checkin.objects.filter(profile=user.profile)
    home = Checkin.objects.filter(profile=request.user.profile)

    if away[0].date <= home[0].date:  # Finds the first date checked in between both users
        first = away[0].date
    else:
        first = home[0].date

    if away.last().date <= home.last().date:  # Finds the most recent checkin between both users
        last = home.last().date
    else:
        last = away.last().date

    step = datetime.timedelta(days=1)
    timeline = []

    while first <= last:
        timeline.append(first)
        first += step

    context = {
        'timeline': timeline,
        'away': away,
        'home': home,
    }
    return render(request, 'pages/compare.html', context)


# @login_required
# def editProfile(request, pk):
#     user = User.objects.get(pk=pk)
#     form = ProfileForm(instance=user)

#     if request.method == 'GET':
#         return render(request, 'pages/editProfile.html')

#     if request.method == 'POST':
#         user = User.objects.get(pk=pk)
#         profile = user.profile
#         form = ProfileForm(instance=profile)

#         if request.user.is_authenticated() and request.user.id == user.id:
#             if request.method == "POST":
#                 form = ProfileForm(request.POST, request.FILES, instance=profile)

#     return render(request, 'pages/edit_profile.html', {'form': form})

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.profile

            if request.POST.get("zip") != "":
                user.zipCode = form.cleaned_data['zipCode']

            if request.POST.get("continent") != "":
                user.continent = form.cleaned_data['continent']

            if request.POST.get("income") != "":
                user.income = form.cleaned_data['income']

            if request.FILES.get('profile_pic'):
                user.profile_pic = form.cleaned_data['profile_pic']

            user.save()
            return profilepage(request)
    else:
        form = ProfileForm()

    return render(request, 'pages/editProfile.html', {'form': form})


@login_required
def checkinpage(request):
    if request.method == 'GET':
        today = datetime.date.today()

        if len(Checkin.objects.filter(profile=request.user.profile, date=today)) != 0:
            return render(request, 'pages/updateCheckin.html')

        else: 
            return render(request, 'pages/checkin.html')

@login_required
def updateCheckin(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == "Replace checkins":
            print("replace")
            today = datetime.date.today()
            checkins = Checkin.objects.filter(profile=request.user.profile, date=today)
            for checkin in checkins:
                checkin.delete()
            return render(request, 'pages/checkin.html')

        else:
            return render(request, 'pages/tallycheckin.html')

def tallyCheckin(request):
    if request.method == 'POST':
        api_list = Impact.objects.all()
        checkin = Checkin.objects.create(score=0)
        today = datetime.date.today()
        footprint = 0
        tallies = Checkin.objects.filter(profile=request.user.profile, date=today)
        for tally in tallies:
            footprint += tally.score
            tally.delete()

        for item in api_list:
            check = request.POST.get(item.item)
            footprint += int(check) * float(item.co2PerUnit)
            Serving.objects.create(container=checkin, key=item, value=int(check))

        checkin.profile = request.user.profile
        checkin.score = round(footprint, 2)
        checkin.save()
            
        
        today = datetime.date.today()
        d = today.strftime("%Y-%m-%d")

        users = User.objects.all()

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

        avg = 0
        checkins = Checkin.objects.filter(profile=request.user.profile)

        for checkin in checkins:
            avg += checkin.score

        if len(checkins):
            avg = round(avg / len(checkins), 2)

        context = {
            'avg': avg,
            'contScores': contScores,
            'zipScores': zipScores,
            'incomeScores': incomeScores,
            'checkins': checkins,
            'users': users,
        }
        return render(request, 'pages/profile.html', context)




@login_required
def add_checkin(request):
    if request.method == 'POST':
        api_list = Impact.objects.all()
        checkin = Checkin.objects.create(score=0)
        footprint = 0
        for item in api_list:
            check = request.POST.get(item.item)
            footprint += int(check) * float(item.co2PerUnit)
            Serving.objects.create(container=checkin, key=item, value=int(check))

        checkin.profile = request.user.profile
        checkin.score = round(footprint, 2)
        checkin.save()

        today = datetime.date.today()
        d = today.strftime("%Y-%m-%d")

        users = User.objects.all()

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

        avg = 0
        checkins = Checkin.objects.filter(profile=request.user.profile)

        for checkin in checkins:
            avg += checkin.score

        if len(checkins):
            avg = round(avg / len(checkins), 2)

        context = {
            'avg': avg,
            'contScores': contScores,
            'zipScores': zipScores,
            'incomeScores': incomeScores,
            'checkins': checkins,
            'users': users,
        }
        return render(request, 'pages/profile.html', context)

    # api_list = Impact.objects.all()
    # today = datetime.date.today()
    # footprint = 0

    # def tally(footprint):
    #     for item in api_list:
    #         check = request.POST.get(item.item)
    #         footprint += int(check) * float(item.co2PerUnit)
    #         Serving.objects.create(container=checkin, key=item, value=int(check))

    # if Checkin.objects.get(user=request.user, date=today):

    #     # ask user if they want to replace or tally

    #     if input == "replace": # deletes all checkins that day, and runs the tally
    #         tallies = Checkin.objects.filter(user=request.user, date=today)
    #         for checkin in tallies:
    #             checkin.delete()
    #         tally()
        
    #     else: # if tally is selected, gets score from all existing checkins that day and tallies from there
    #         tallies = Checkin.objects.filter(user=request.user, date=today)
    #         for checkin in tallies:
    #             footprint += checkin.score
    #             tally()
    
    # else: # if no checkins exist for that day, runs tally
    #     checkin = Checkin.objects.create(score=0)
    #     tally()

    # checkin.profile = request.user.profile
    # checkin.score = round(footprint, 2)
    # checkin.save()

    # return redirect('checkin')


@login_required
def user_index(request):
    user_list = User.objects.all()

    context = {
        'user_list': user_list
    }

    return render(request, 'pages/index.html', context)