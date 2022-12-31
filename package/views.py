from django.shortcuts import render
from .models import PackageSubscriptions
from .serializers import PackageSubscriptionSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PackageSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = PackageSubscriptions.objects.all()
    serializer_class = PackageSubscriptionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]