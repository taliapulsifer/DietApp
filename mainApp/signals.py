from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from .models import DailyTotal

@receiver(user_logged_in)

def macroReset(sender, request, user, **kwargs):
    today = timezone.now().date()
    dailyTotal, created = DailyTotal.objects.get_or_create(user=user, date=today)

    if created:
        dailyTotal.total_calories = 0
        dailyTotal.total_protein = 0
        dailyTotal.total_carbs = 0
        dailyTotal.total_fats = 0
        dailyTotal.total_sugar = 0
        dailyTotal.total_sodium = 0
        dailyTotal.save()

    #See what the last login was
    lastLogIn = request.session.get('lastLogIn')
    #Check to see if the date has changed
    if lastLogIn != timezone.now().date():
        dailyTotal.total_calories = 0
        dailyTotal.total_protein = 0
        dailyTotal.total_carbs = 0
        dailyTotal.total_fats = 0
        dailyTotal.total_sugar = 0
        dailyTotal.total_sodium = 0
        dailyTotal.save()

        request.session['lastLogIn'] = str(today)