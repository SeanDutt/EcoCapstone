from django.db import models

# Create your models here.

class Impact(models.Model):
  CATEGORIES = [
    ('Meat', 'Meat'),
    ('Produce', 'Produce'),
    ('Dairy', 'Dairy'),
    ('Beverages', 'Beverages'),
    ('Misc. Food', 'Misc. Food'),
    ('Other', 'Other'),
]

  item = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  co2PerUnit = models.FloatField(max_length=100)
  category = models.CharField(max_length=25, choices=CATEGORIES, default='Misc. Food')

  def __str__(self):
    return self.item