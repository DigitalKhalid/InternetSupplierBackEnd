from django.shortcuts import render
from .models import Connection
from .serializers import ConnectionSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F

# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# from .throttling import CustomerRateThrottle

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all().annotate(customer_name = F('customer__first_name'))
    serializer_class = ConnectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # authentication_classes = [JWTAuthentication]
    # throttle_classes = [UserRateThrottle, CustomerRateThrottle]
    # throttle_classes = [CustomerRateThrottle]


