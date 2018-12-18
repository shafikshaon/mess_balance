from django.urls import path

from bazaar.views import BazaarCreateView, BazaarListView, BazaarUpdateView, BazaarSearchView

urlpatterns = [
    path('add/', BazaarCreateView.as_view(), name='bazaar-add'),
    path('list/', BazaarListView.as_view(), name='bazaar-list'),
    path('search/', BazaarSearchView.as_view(), name='bazaar-search'),
    path('update/<pk>', BazaarUpdateView.as_view(), name="bazaar-update"),
]
