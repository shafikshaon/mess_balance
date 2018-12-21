import datetime

from django import forms
from django.utils.translation import gettext as _

from accounts.models import User
from meals.models import Meal

BREAKFAST_MEAL_COUNT = (
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
)

LUNCH_DINNER_MEAL_COUNT = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

MONTHS = {
    1: _('Jan'), 2: _('Feb'), 3: _('Mar'), 4: _('Apr'),
    5: _('May'), 6: _('Jun'), 7: _('Jul'), 8: _('Aug'),
    9: _('Sep'), 10: _('Oct'), 11: _('Nov'), 12: _('Dec')
}

current_year = str(datetime.date.today().year)
next_year = str(datetime.date.today().year + 1)


class AddMealForm(forms.ModelForm):
    meal_date = forms.DateField(
        label='Add meal for',
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    breakfast = forms.ChoiceField(choices=BREAKFAST_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                                  initial=0.5)
    lunch = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                              initial=1)
    dinner = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}),
                               initial=1)

    class Meta:
        model = Meal
        fields = ('meal_date', 'breakfast', 'lunch', 'dinner')


class UpdateMealForm(forms.ModelForm):
    meal_date = forms.DateField(
        label='Update meal for',
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    breakfast = forms.ChoiceField(choices=BREAKFAST_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}))
    lunch = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}))
    dinner = forms.ChoiceField(choices=LUNCH_DINNER_MEAL_COUNT, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Meal
        fields = ('meal_date', 'breakfast', 'lunch', 'dinner')


class MealSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MealSearchForm, self).__init__(*args, **kwargs)
        self.fields['member'].label_from_instance = lambda obj: "%s" % obj.get_full_name()

    member = forms.ModelChoiceField(
        initial='',
        queryset=User.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    from_date = forms.DateField(
        label='From date',
        initial=datetime.date.today,
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control'}))
    to_date = forms.DateField(
        label='To date',
        initial=datetime.date.today,
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control'}))

    class Meta:
        model = Meal
        fields = ('member', 'from_date', 'to_date')
