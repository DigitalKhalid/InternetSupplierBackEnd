from django.shortcuts import render
from .models import Product, ProductCatagory, ProductType, Unit
from .serializers import ProductSerializer, ProductSerializerRelated, UnitSerializer, ProductCatagorySerializer, ProductTypeSerializer, PackageListSerializer, ProductListSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from customizations.pagination import CustomPagination
from django.db.models import Q, F


class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ProductViewSetRelated(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['id', 'catagory__title', 'catagory__type__title']
    search_fields = ['title', 'sku', 'description', 'catagory__title', 'catagory__type__title', 'unit__title', 'sale_price']
    ordering_fields = ['title', 'sku', 'description', 'sale_price', 'unit__title']
    ordering = 'title'


class PackageList(viewsets.ModelViewSet):
    queryset = Product.objects.filter(Q(catagory__type__title='Package'))
    serializer_class = PackageListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering = 'title'


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.filter(~Q(catagory__type__title='Package'))\
        .annotate(catagory_title = F('catagory__title'))\
        .annotate(product_type = F('catagory__type__title'))
    serializer_class = ProductListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering = 'title'

class CatagoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCatagory.objects.all()
    serializer_class = ProductCatagorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type__title']
    search_fields = ['title', 'type__title']
    ordering_fields = ['title', 'type__title']
    ordering = 'title'

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['value']
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = 'title'