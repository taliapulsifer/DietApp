from django import forms
from .models import Meal, MealItem

class FoodItemForm(forms.ModelForm):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    mealType = forms.ChoiceField(choices=MEAL_CHOICES)

    name = forms.CharField(max_length=100, help_text="Enter the name of the meal, e.g 'Sandwich' or 'Matcha'.")

    class Meta:
        model = MealItem
        fields = ['name', 'calories', 'protein', 'carbs', 'fats', 'salt', 'sugars', 'salt', 'servingSize', 'quantity']