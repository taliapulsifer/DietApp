from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DailyTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    total_calories = models.FloatField(default=0)
    total_protein = models.FloatField(default=0)
    total_carbs = models.FloatField(default=0)
    total_sugar = models.FloatField(default=0)
    total_sodium = models.FloatField(default=0)
    total_fats = models.FloatField(default=0)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username}'s totals for {self.date}"

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mealType = models.CharField(max_length=100, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'),
                                                        ('Dinner', 'Dinner'), ('Snack', 'Snack'), ('Drink', 'Drink')],
                                                        default='Snack', null = True)
    date = models.DateField(default=timezone.now)

class MealItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    calories = models.FloatField(default = 0)
    protein = models.FloatField(default = 0)
    carbs = models.FloatField(default = 0)
    fats = models.FloatField(default = 0)
    sugars = models.FloatField(default = 0)
    salt = models.FloatField(default = 0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dailyCalories = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    currentWeight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    goalWeight = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name