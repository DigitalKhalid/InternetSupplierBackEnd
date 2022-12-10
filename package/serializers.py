from rest_framework import serializers
from .models import PackageSubscriptions


class PackageSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageSubscriptions
        fields = '__all__'