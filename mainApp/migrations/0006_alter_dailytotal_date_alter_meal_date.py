# Generated by Django 5.1.1 on 2024-09-23 02:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_mealitem_date_alter_meal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytotal',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
