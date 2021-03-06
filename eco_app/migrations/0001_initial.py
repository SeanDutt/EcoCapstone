# Generated by Django 3.2.3 on 2021-06-26 04:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eco_app.checkin')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipCode', models.CharField(blank=True, max_length=10, null=True)),
                ('continent', models.CharField(blank=True, max_length=20, null=True)),
                ('income', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkin',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eco_app.profile'),
        ),
    ]
