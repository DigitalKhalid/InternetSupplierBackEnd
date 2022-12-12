from django.shortcuts import render
from .models import Connection
from .serializers import ConnectionSerializer, ConnectionSerializerRelated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F, Case, When, Max, Min
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
import datetime

# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# from .throttling import CustomerRateThrottle


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ConnectionViewSetRelated(viewsets.ModelViewSet):
    queryset = Connection.objects.all()\
        .annotate(active_subscription=(Case(When(Q(subscriptions__activation_date__lte=datetime.date.today()) & Q(subscriptions__expiry_date__gte=datetime.date.today()), then='subscriptions__id'))))\
        .annotate(expiry_date=Min(Case(When(active_subscription__isnull=True,then=None), When(active_subscription__isnull=False, then='subscriptions__expiry_date'))))\
        .annotate(subscription_id=Min(Case(When(active_subscription__isnull=True,then=None), When(active_subscription__isnull=False, then='subscriptions__id'))))

    serializer_class = ConnectionSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['status', 'subscriptions__status',
                        'subscriptions__expiry_date']
    search_fields = ['connection_id', 'installation_date',
                     '^status', 'customer__first_name', 'customer__last_name']
