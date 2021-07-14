from django.core.management.base import BaseCommand
from ...models import Impact
import csv

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
      with open(food.csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
          if line_count == 0:
            line_count += 1
          else:
            Impact.objects.create(item={row[0]},co2PerUnit=float({row[1]}))
            line_count += 1