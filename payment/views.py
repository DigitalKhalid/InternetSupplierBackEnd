from .models import Payment
from .serializers import PaymentSerializer, PaymentSerializerRelated
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSetRelated(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerRelated
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['payment_type', 'order__order_id', 'date_created']
    ordering_fields = ['payment_type', 'order__order_id', 'date_created']
    ordering = ('-date_created')