# Generated by Django 3.2.3 on 2021-06-11 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_app', '0016_alter_checkin_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
