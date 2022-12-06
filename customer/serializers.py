from rest_framework import serializers
from .models import Customer
from location.serializers import SubAreaSerializerRelated
# from connection.serializers import ConnectionSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerSerializerRelated(serializers.ModelSerializer):
    subarea = SubAreaSerializerRelated(read_only=True)
    # connections = 'connections__connection_id'

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'contact',
            'email',
            'biography',
            'street_address',
            'subarea',
            'connections']