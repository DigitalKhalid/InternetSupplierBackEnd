from customer.serializers import CustomerSerializer
from rest_framework import serializers
from .models import Connection
from location.serializers import SubAreaSerializer


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


class ConnectionSerializerRelated(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    subarea = SubAreaSerializer(many=False)

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'installation_date',
                  'subarea', 'package', 'status', 'new', 'customer']
