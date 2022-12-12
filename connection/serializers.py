from customer.serializers import CustomerSerializer
from rest_framework import serializers
from .models import Connection
from location.serializers import SubAreaSerializer
from product.serializers import ProductSerializer
from package.serializers import PackageSubscriptionSerializer


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


class ConnectionSerializerRelated(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    subarea = SubAreaSerializer(many=False)
    package = ProductSerializer(read_only=True)
    expiry_date = serializers.DateField(read_only=True)
    subscription_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'installation_date',
                  'subarea', 'package', 'status', 'new', 'customer', 'expiry_date','subscription_id']
