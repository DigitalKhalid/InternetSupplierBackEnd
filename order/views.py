from .models import Order, OrderDetail, OrderPackageDetail
from .serializers import OrderSerializer, OrderSerializerRelated, OrderDetailSerializer, OrderDetailSerializerRelated, InvoiceSerializer, OrderSerialSerializer, OrderPackageDetailSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
from django.db.models import F, Count, Sum, Max, Q, Case, When

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderPackageDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderPackageDetail.objects.all()
    serializer_class = OrderPackageDetailSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSetRelated(viewsets.ModelViewSet):
    queryset = Order.objects.all()\
        .annotate(payment_count = Count(F('payments__id')))
    serializer_class = OrderSerializerRelated
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['id']
    search_fields = ['order_id', 'date_created', 'connection__connection_id', 'status']
    ordering_fields = ['order_id', 'date_created', 'connection__connection_id', 'value', 'status']

# Get order serial to generate new order ID
class OrderSerialViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialSerializer
    permission_classes = [IsAuthenticated]


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

class OrderDetailViewSetRelated(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializerRelated
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order']
    search_fields = ['product', 'product__title', 'product__sku']
    ordering_fields = ['product', 'product__title', 'product__sku']

# Invoice
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()\
        .annotate(payment_count = Count(F('payments__id')))\
        .annotate(payment_received = Sum(F('payments__amount')))
        # .annotate(value = Sum(F('details__qty')*F('details__sale_price')))
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']