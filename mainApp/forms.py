from django import forms
from .models import Meal, MealItem, Profile

class FoodItemForm(forms.ModelForm):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    name = forms.CharField(max_length=100, help_text="Enter the name of the meal, e.g 'Sandwich' or 'Matcha'.", required=True)
    mealType = forms.ChoiceField(choices=MEAL_CHOICES)
    calories = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    protein = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    carbs = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    fats = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    sugars = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    class Meta:
        model = MealItem
        fields = ['name', 'mealType','calories', 'protein', 'carbs', 'fats', 'salt', 'sugars', 'salt']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'dailyCalories', 'currentWeight', 'goalWeight']
