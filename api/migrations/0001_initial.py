# Generated by Django 3.2.3 on 2021-05-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('co2PerUnit', models.FloatField(max_length=100)),
                ('category', models.CharField(choices=[('Meat', 'Meat'), ('Produce', 'Produce'), ('Dairy', 'Dairy'), ('Beverages', 'Beverages'), ('Misc. Food', 'Misc. Food'), ('Other', 'Other')], default='Misc. Food', max_length=25)),
            ],
        ),
    ]
