from django.shortcuts import render
from .models import Connection
from .serializers import ConnectionSerializer, ConnectionSerializerRelated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# from .throttling import CustomerRateThrottle

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ConnectionViewSetRelated(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['connection_id', 'installation_date', '^status', 'customer__first_name', 'customer__last_name']