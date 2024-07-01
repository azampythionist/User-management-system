from django.urls import path
from .views import HomeView, UserListCreateView, UserDetailUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users', UserListCreateView.as_view(), name='create-user'),
    path('users/<int:id>', UserDetailUpdateView.as_view(), name='detail-update-user'),
]
