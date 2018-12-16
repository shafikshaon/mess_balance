from django.urls import path

from meals.views import MealCreateView, MealListView, MealUpdateView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('update/<pk>', MealUpdateView.as_view(), name="meal-update"),
]
