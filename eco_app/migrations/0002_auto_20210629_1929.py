# Generated by Django 3.2.3 on 2021-06-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='continent',
            field=models.CharField(blank=True, default='Asia', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.CharField(blank=True, default='0 to 10k', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipCode',
            field=models.CharField(blank=True, default='12345', max_length=10, null=True),
        ),
    ]
