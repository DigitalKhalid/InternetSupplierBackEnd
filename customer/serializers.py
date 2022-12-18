from rest_framework import serializers
from .models import Customer
from location.serializers import SubAreaSerializerRelated


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerInvoiceSerializer(serializers.ModelSerializer):
    subarea = SubAreaSerializerRelated(read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id',
            'first_name',
            'last_name',
            'contact',
            'email',
            'biography',
            'street_address',
            'subarea']
            
from connection.serializers import ConnectionSerializer
class CustomerSerializerRelated(serializers.ModelSerializer):
    subarea = SubAreaSerializerRelated(read_only=True)
    connections = ConnectionSerializer(read_only=True, many=False)

    class Meta:
        model = Customer
        fields = [
            'id',
            'first_name',
            'last_name',
            'contact',
            'email',
            'biography',
            'street_address',
            'subarea',
            'connections']
