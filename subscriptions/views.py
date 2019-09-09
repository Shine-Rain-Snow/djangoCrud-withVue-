from django.shortcuts import render
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import generics
# Create your views here.

class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
