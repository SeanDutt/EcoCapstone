from django.db import models
from django.db.models.fields import CharField, FloatField

# Create your models here.

class FoodItem(models.Model):
  FOOD_CATEGORIES = [
    ('Meat', 'Meat'),
    ('Produce', 'Produce'),
    ('Dairy', 'Dairy'),
    ('Beverages', 'Beverages'),
    ('Other', 'Other'),
]
  item = CharField(max_length=100)
  co2PerServing = FloatField(max_length=100)
  category = models.CharField(max_length=25, choices=FOOD_CATEGORIES, default='Other')

  def __str__(self):
    return self.item