from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderSerializerRelated, OrderDetailSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination


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
    search_fields = ['order_id', 'date_created', 'connection__connection_id', 'value', 'status']
    ordering_fields = ['order_id', 'date_created', 'connection__connection_id', 'value', 'status']

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]