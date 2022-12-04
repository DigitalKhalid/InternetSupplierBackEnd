from django.shortcuts import render
from .models import Country, City, Area, SubArea
from .serializers import CountrySerializer, CitySerializer, CitySerializerRelated, AreaSerializer, AreaSerializerRelated, SubAreaSerializer, SubAreaSerializerRelated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['country']


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

class CityViewSetRelated(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country']
    search_fields = ['city', 'country__country']
    ordering_fields = ['city', 'country__country']


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

class AreaViewSetRelated(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['city']
    search_fields = ['area', 'city__city', 'city__country__country']
    ordering_fields = ['area', 'city__city', 'city__country__country']


class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

class SubAreaViewSetRelated(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializerRelated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['subarea', 'area__area', 'area__city__city', 'area__city__country__country']
    ordering_fields = ['subarea', 'area__area', 'area__city__city', 'area__city__country__country']
