# Generated by Django 5.1.1 on 2024-09-26 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='mealitem',
            name='servingSize',
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='mainApp.meal'),
        ),
    ]
