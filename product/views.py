from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, ProductSerializerRelated, UnitSerializer, ProductCatagorySerializer, ProductTypeSerializer, PackageListSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination


class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ProdcutViewSetRelated(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['id', 'catagory__title']
    search_fields = ['title', 'sku', 'description', 'catagory__title']
    ordering_fields = ['title', 'sku', 'description', 'sale_price']
    ordering = 'catagory__title'


class PackageList(viewsets.ModelViewSet):
    queryset = Product.objects.filter(catagory__title='Package')
    serializer_class = PackageListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering = 'title'