from rest_framework import serializers
from .models import Connection
from customer.models import Customer
from customer.serializers import CustomerSerializer


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'