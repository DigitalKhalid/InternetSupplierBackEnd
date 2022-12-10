from django.shortcuts import render
from .models import PackageSubscriptions
from .serializers import PackageSubscriptionSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
import datetime


class PackageViewSetRelated(viewsets.ModelViewSet):
    queryset = PackageSubscriptions.objects.filter(expiry_date__lt = datetime.datetime.today())
    serializer_class = PackageSubscriptionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['catagory__title']
    search_fields = ['title', 'sku', 'description', 'catagory__title']
    ordering_fields = ['title', 'sku', 'description', 'sale_price']