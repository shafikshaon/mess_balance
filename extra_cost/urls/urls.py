from django.urls import path

from extra_cost.views import ExtraCostUpdateView, ExtraCostListView, ExtraCostCreateView

urlpatterns = [
    path('add/', ExtraCostCreateView.as_view(), name='extra_cost-add'),
    path('list/', ExtraCostListView.as_view(), name='extra_cost-list'),
    path('update/<pk>', ExtraCostUpdateView.as_view(), name="extra_cost-update"),
]
