# Generated by Django 3.2.3 on 2021-06-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_app', '0024_auto_20210617_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
