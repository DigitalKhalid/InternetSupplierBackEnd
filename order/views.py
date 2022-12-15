from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderSerializerRelated, OrderDetailSerializer, OrderDetailSerializerRelated
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
from django.db.models import F, Sum

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSetRelated(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerRelated
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['order_id', 'date_created', 'connection__connection_id', 'status']
    ordering_fields = ['order_id', 'date_created', 'connection__connection_id', 'value', 'status']

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