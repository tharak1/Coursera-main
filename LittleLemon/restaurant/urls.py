from django.urls import path
from .views import UserListAPIView, MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('menu/', MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', BookingView.as_view()),

]