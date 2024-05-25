from django.shortcuts import render
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from .models import *

class UserListAPIView(generics.ListCreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuItemView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
