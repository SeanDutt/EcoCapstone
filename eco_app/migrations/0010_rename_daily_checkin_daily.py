# Generated by Django 3.2.3 on 2021-06-04 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eco_app', '0009_alter_daily_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='Daily',
            new_name='daily',
        ),
    ]
