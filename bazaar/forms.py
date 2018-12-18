import datetime

from django import forms
from django.utils.translation import gettext as _

from accounts.models import User
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


class BazaarSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BazaarSearchForm, self).__init__(*args, **kwargs)
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
        model = Bazaar
        fields = ('member', 'from_date', 'to_date')
