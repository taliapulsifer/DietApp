from collections import defaultdict

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .forms import FoodItemForm, ProfileForm
from .models import Meal, DailyTotal, Profile
from django.db.models import Sum
from django.utils import timezone

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('nutrition_app:home')
        return render(request, 'nutrition/login.html', {
            'form': form,
            'error': 'Invalid username or password'  # Show error on the login page
        })
    else:
        form = AuthenticationForm()

    return render(request, 'nutrition/login.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.name = form.cleaned_data['name']
            profile.dailyCalories = form.cleaned_data['dailyCalories']
            profile.currentWeight = form.cleaned_data['currentWeight']
            profile.goalWeight = form.cleaned_data['goalWeight']
            profile.save()

            return redirect('nutrition_app:home')  # Redirect to home or any other page after saving
    else:
        # If the user already has a profile, pre-populate the form with existing data
        try:
            profile = Profile.objects.get(user=request.user)
            form = ProfileForm(instance=profile)
        except Profile.DoesNotExist:
            form = ProfileForm()

    return render(request, 'nutrition/profile.html', {'form': form})

def home(request):
    if not request.user.is_authenticated:
        return redirect('nutrition_app:login')
    today = timezone.now().date()
    daily_total, created = DailyTotal.objects.get_or_create(user=request.user, date=today)
    meals = Meal.objects.filter(user=request.user, date=today)

    # Calculate totals
    total_calories = meals.aggregate(Sum('items__calories'))['items__calories__sum'] or 0
    total_protein = meals.aggregate(Sum('items__protein'))['items__protein__sum'] or 0
    total_carbs = meals.aggregate(Sum('items__carbs'))['items__carbs__sum'] or 0
    total_fats = meals.aggregate(Sum('items__fats'))['items__fats__sum'] or 0
    total_sugar = meals.aggregate(Sum('items__sugars'))['items__sugars__sum'] or 0
    total_sodium = meals.aggregate(Sum('items__salt'))['items__salt__sum'] or 0

    # Update the daily total
    daily_total.total_calories = total_calories
    daily_total.total_protein = total_protein
    daily_total.total_carbs = total_carbs
    daily_total.total_fats = total_fats
    daily_total.total_sugar = total_sugar
    daily_total.total_sodium = total_sodium
    daily_total.save()

    meal_items_names = []
    #For every food item that has been added
    for meal in meals:
        meal_items = meal.items.all()
        meal_items_names.extend([item.name for item in meal_items])

    context = {
        'meal_item_names' : meal_items_names,
        'meals': meals,
        'total_calories': daily_total.total_calories,
        'total_protein': daily_total.total_protein,
        'total_carbs': daily_total.total_carbs,
        'total_fats': daily_total.total_fats,
        'total_sodium': daily_total.total_sodium,
        'total_sugar': daily_total.total_sugar,
    }

    return render(request, 'nutrition/home.html', context)


def foodForm(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            calories = form.cleaned_data.get('calories') or 0
            protein = form.cleaned_data.get('protein') or 0
            carbs = form.cleaned_data.get('carbs') or 0
            fats = form.cleaned_data.get('fats') or 0
            sugars = form.cleaned_data.get('sugars') or 0

            # Get the meal type from the form data
            mealType = form.cleaned_data.get('mealType')

            # Create or get the meal for today
            meal, created = Meal.objects.get_or_create(
                mealType=mealType,
                date=timezone.now().date(),
                user=request.user
            )

            # Create a meal item and associate it with the meal
            meal_item = form.save(commit=False)
            meal_item.meal = meal
            meal_item.save()

            return redirect('nutrition_app:home')
    else:
        form = FoodItemForm()

    return render(request, 'nutrition/FoodItemForm.html', {'form': form})


def meals_history(request):
    if request.user.is_authenticated:
        # Fetch meals for the logged-in user and prefetch related MealItems
        meals = Meal.objects.filter(user=request.user).prefetch_related('items').order_by('date')
    else:
        meals = []

    # Prepare the context for rendering
    organized_meals = []  # List to hold meal data
    for meal in meals:
        meal_items = meal.items.all()  # Get related MealItems
        organized_meals.append({
            'date': meal.date,
            'meal_type': meal.mealType,
            'meal_items': meal_items,
        })

    print(organized_meals)  # For debugging the structure

    # Pass the organized meals to the template
    return render(request, 'nutrition/history.html', {'organized_meals': organized_meals})