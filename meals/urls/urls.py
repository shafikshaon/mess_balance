from django.urls import path

from meals.views import MealCreateView, MealListView, MealUpdateView, MealSearchView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('search/', MealSearchView.as_view(), name='meal-search'),
    path('update/<pk>', MealUpdateView.as_view(), name="meal-update"),
]
