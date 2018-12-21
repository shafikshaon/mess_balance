from django.urls import path

from extra_cost.views import ExtraCostUpdateView, ExtraCostListView, ExtraCostCreateView, ExtraCostSearchView, \
    AccountingExtraCostListView

urlpatterns = [
    path('add/', ExtraCostCreateView.as_view(), name='extra_cost-add'),
    path('list/', ExtraCostListView.as_view(), name='extra_cost-list'),
    path('accounting/list/', AccountingExtraCostListView.as_view(), name='accounting-extra_cost-list'),
    path('search/', ExtraCostSearchView.as_view(), name='extra_cost-search'),
    path('update/<pk>', ExtraCostUpdateView.as_view(), name="extra_cost-update"),
]
