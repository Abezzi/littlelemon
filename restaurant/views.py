from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, "index.html", {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 