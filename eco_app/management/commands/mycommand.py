from django.contrib.auth.models import User
from ...models import Checkin, Serving, Profile
from django.core.management.base import BaseCommand
import random as r
from datetime import date, timedelta



class Command(BaseCommand):

  def baby_name(self):
    prefix_list = ["Da","Ka","Sha","Ma","Gla","Tre","Ru","Ron","Tu","Sue","Fo","Jo","Jenni","Po","Minni","Deli","Aissa","Mai","Jeze","Ja","Sa","Diy","Ami","Sala","Oli","Dem","Li","Ev","Ah","Moha","Ahme","Kaja","Na","Jona","Regi","Sher","A","Sa","Ma","Ta","Shel","Wil","Rag","Ud","Uth","Aga","Ab","Dah","Bre"]
    suffix_list = ["ren","ron","ana","lyn","da","paul","ra","bu","bob","role","tana","nissa","aqua","ray","lah","tou","mouna","bel","din","ya","nata","ba","med","lith","a","vi","via","ver","than","nald","lock","sha","ley","son","nar","red","tha","dou","by","lia","ria","von","onna","doul","mad"]
    prefix = r.choice(prefix_list)
    suffix = r.choice(suffix_list)
    name = prefix+suffix
    return name

  def income(self):
    income_list = ["0 to 10k", "10k to 20k", "20k to 40k", "40k to 60k", "60k to 80k", "80k to 100k", "100k to 150k", "Over 150k"]
    income = r.choice(income_list)
    return income

  def continent(self):
    continent_list = ["Asia", "Africa", "Europe", "North America", "South America", "Australia/Oceania", "Antarctica"]
    continent = r.choice(continent_list)
    return continent

  def zip(self):
    zip_list = ["97218", "98661", "97313", "97217", "98765"]
    zip_code = r.choice(zip_list)
    return zip_code

  def daterange(self, start_date, end_date):
    for i in range(int((end_date - start_date).days)):
      yield start_date + timedelta(i)

  def add_arguments(self, parser):
    parser.add_argument('total', type=int, help='Indicates the number of users to be created')

  def handle(self, *args, **kwargs):
    total = kwargs['total']
    for i in range(total):
      user = User.objects.create_user(username=self.baby_name(), email='', password='123')
      profile = Profile.objects.create(user=user)
      profile.zipCode = self.zip()
      profile.continent = self.continent()
      profile.income = self.income()
      profile.save()

      start_date = date(2021, 6, 1)
      end_date = date(2021, 7, 16)

      for day in self.daterange(start_date, end_date):
        Checkin.objects.create(profile=profile, date=day, score=r.randint(1, 20))

