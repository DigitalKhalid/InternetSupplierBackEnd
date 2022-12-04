from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer, CustomerSerializerRelated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import CustomerRateThrottle

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle, CustomerRateThrottle]
    throttle_classes = [CustomerRateThrottle]

class CustomerViewSetRelated(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomerRateThrottle]