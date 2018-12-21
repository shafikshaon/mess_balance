"""mess_balance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls.static import static
from django.urls import path, include

from core.views.dashboard import DashboardView
from core.views.reckoning import ReckoningView
from mess_balance import settings

urlpatterns = [
    path('', DashboardView.as_view()),
    path('reckoning/', ReckoningView.as_view(), name='reckoning'),
    path('accounts/', include('accounts.urls')),
    path('meals/', include('meals.urls')),
    path('bazaar/', include('bazaar.urls')),
    path('extra_cost/', include('extra_cost.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
