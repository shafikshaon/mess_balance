from django.urls import path

from meals.views import MealCreateView, MealListView, MealUpdateView, MealSearchView, AccountingMealListView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('accounting/list/', AccountingMealListView.as_view(), name='accounting-meal-list'),
    path('search/', MealSearchView.as_view(), name='meal-search'),
    path('update/<pk>', MealUpdateView.as_view(), name="meal-update"),
]
