import datetime

from django import forms
from django.utils.translation import gettext as _

from bazaar.models import Bazaar

current_year = str(datetime.date.today().year)
next_year = str(datetime.date.today().year + 1)

MONTHS = {
    1: _('Jan'), 2: _('Feb'), 3: _('Mar'), 4: _('Apr'),
    5: _('May'), 6: _('Jun'), 7: _('Jul'), 8: _('Aug'),
    9: _('Sep'), 10: _('Oct'), 11: _('Nov'), 12: _('Dec')
}


class AddBazaarForm(forms.ModelForm):
    bazaar_date = forms.DateField(
        label='Add bazaar for',
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                   initial=1.0)
    item_price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  initial=1.0)

    class Meta:
        model = Bazaar
        fields = ('bazaar_date', 'item_name', 'item_weight', 'item_price')


class UpdateBazaarForm(forms.ModelForm):
    bazaar_date = forms.DateField(
        label='Update bazaar for',
        widget=forms.SelectDateWidget(
            years=(current_year, next_year),
            months=MONTHS,
            attrs={'class': 'form-control d-inline w-30 mr-2'}),
        initial=datetime.datetime.now)
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                   initial=1.0)
    item_price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  initial=1.0)

    class Meta:
        model = Bazaar
        fields = ('bazaar_date', 'item_name', 'item_weight', 'item_price')
