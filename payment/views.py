from .models import Payment
from .serializers import PaymentSerializer, PaymentSerializerRelated, PaymentInvoiceSerializer, PaymentDashboardSerializer, PaymentHistoryDashboardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
from django.db.models.functions import Concat, TruncMonth
from django.db.models import Value, F, Case, When, Sum, Q
from datetime import date


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDashboardViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.aggregate(total_payment= Sum('amount'))
    serializer_class = PaymentDashboardSerializer
    permission_classes = [IsAuthenticated]


class PaymentHistoryDashboardViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.annotate(payment_month=TruncMonth('date_created__date')).values('payment_month').annotate(total_amount=Sum('amount'))
    serializer_class = PaymentHistoryDashboardSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSetRelated(viewsets.ModelViewSet):
    queryset = Payment.objects.all()\
        .annotate(cashier_name =F('received_by__username'))\
        .annotate(connection_id = F('order__connection__connection_id'))
    serializer_class = PaymentSerializerRelated
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['payment_type', 'order__order_id', 'date_created', 'received_by__first_name', 'received_by__first_name', 'order__connection__connection_id']
    ordering_fields = ['payment_type', 'order__order_id', 'date_created', 'received_by__first_name', 'order__connection__connection_id']
    ordering = ('-date_created')

# class PaymentInvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentInvoiceSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['id']