from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer, CustomerSerializerRelated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomerViewSetRelated(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(customer_type='Individual')
    serializer_class = CustomerSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['first_name', 'last_name', 'street_address', 'contact', 'email', 'subarea__area__area', 'subarea__area__city__city', 'subarea__area__city__country__country']
    ordering_fields = ['first_name', 'last_name', 'subarea__area__area']


class DealerViewSetRelated(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(customer_type='Dealer')
    serializer_class = CustomerSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['first_name', 'last_name', 'street_address', 'contact', 'email', 'subarea__area__area', 'subarea__area__city__city', 'subarea__area__city__country__country']
    ordering_fields = ['first_name', 'last_name', 'subarea__area__area']
