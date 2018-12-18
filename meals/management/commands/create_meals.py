from django.core.management.base import BaseCommand

from meals.models import Meal


class Command(BaseCommand):
    help = 'Create new meals'

    def handle(self, *args, **kwargs):
        Meal.objects.create(user_id=1, meal_date='2018-12-01', breakfast=0.5, lunch=0, dinner=1)
        Meal.objects.create(user_id=1, meal_date='2018-12-02', breakfast=1, lunch=1, dinner=1)
        Meal.objects.create(user_id=1, meal_date='2018-12-03', breakfast=1, lunch=1, dinner=1)
        Meal.objects.create(user_id=1, meal_date='2018-12-04', breakfast=0, lunch=1, dinner=0)
        Meal.objects.create(user_id=1, meal_date='2018-12-05', breakfast=1, lunch=0, dinner=0)

        Meal.objects.create(user_id=2, meal_date='2018-12-01', breakfast=0, lunch=0, dinner=1)
        Meal.objects.create(user_id=2, meal_date='2018-12-02', breakfast=0.5, lunch=1, dinner=1)
        Meal.objects.create(user_id=2, meal_date='2018-12-03', breakfast=1, lunch=1, dinner=1)
        Meal.objects.create(user_id=2, meal_date='2018-12-04', breakfast=0.5, lunch=0, dinner=0)
        Meal.objects.create(user_id=2, meal_date='2018-12-05', breakfast=1, lunch=0, dinner=0)
