from django.urls import path

from accounts.views import LoginView, LogoutView, UserCreateView, UserListView, UserUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/list/', UserListView.as_view(), name='user-list'),
    path('user/update/<pk>', UserUpdateView.as_view(), name="user-update"),
]
