from .models import Setting
from .serializers import SettingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.filter(id=1)
    serializer_class = SettingSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # search_fields = '__all__'