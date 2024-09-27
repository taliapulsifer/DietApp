# Generated by Django 5.1.1 on 2024-09-23 02:02

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_meal_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2024, 9, 23))),
                ('total_calories', models.FloatField()),
                ('total_protein', models.FloatField()),
                ('total_carbs', models.FloatField()),
                ('total_sugar', models.FloatField()),
                ('total_sodium', models.FloatField()),
                ('total_fats', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'date')},
            },
        ),
    ]
