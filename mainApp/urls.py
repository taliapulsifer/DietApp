from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'nutrition_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('foodForm/', views.foodForm, name='foodForm'),
    path('logout/', LogoutView.as_view(next_page='nutrition_app:login'), name='logout'),
    path('nutrition/', views.meals_history, name='mealsList'),
    path('profile/', views.profile, name='profile'),
]

