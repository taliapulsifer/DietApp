from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import MealItem, Meal

admin.site.register(MealItem)
admin.site.register(Meal)

