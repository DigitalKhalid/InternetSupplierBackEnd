from customer.serializers import CustomerSerializer
from rest_framework import serializers
from .models import Connection
from location.serializers import SubAreaSerializer
from product.serializers import ProductSerializer
# from package.serializers import PackageSubscriptionSerializer
from django.db.models import Q, Count


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

class ConnectionDashboardSerializer(serializers.ModelSerializer):
    archived_count = serializers.SerializerMethodField()
    active_count = serializers.SerializerMethodField()
    inactive_count = serializers.SerializerMethodField()

    class Meta:
        model = Connection
        fields = ['archived_count', 'active_count', 'inactive_count']

    def get_archived_count(self, obj):
        archivedcount = Connection.objects.all().aggregate(archived_count=Count('pk', filter=Q(archived = True)))
        return archivedcount["archived_count"]

    def get_active_count(self, obj):
        activecount = Connection.objects.all().aggregate(active_count=Count('pk', filter=Q(status = 'Active', archived = False)))
        return activecount["active_count"]
    
    def get_inactive_count(self, obj):
        inactivecount = Connection.objects.all().aggregate(inactive_count=Count('pk', filter=Q(status = 'Inactive', archived = False)))
        return inactivecount["inactive_count"]


class ConnectionListSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField()

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'customer_name']


class ActiveExpiredConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id']

class ActiveValidConnectionSerializer(serializers.ModelSerializer):
    package = ProductSerializer(read_only=True)
    expiry_date = serializers.DateField(read_only=True)
    subscription_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'expiry_date', 'subscription_id', 'package']


class ConnectionSerializerRelated(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    subarea = SubAreaSerializer(many=False)
    package = ProductSerializer(read_only=True)
    expiry_date = serializers.DateField(read_only=True)
    temp_expiry_date = serializers.DateField(read_only=True)
    subscription_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'installation_date',
                  'subarea', 'package', 'status', 'renewal', 'archived', 'new', 'customer', 'expiry_date', 'temp_expiry_date', 'subscription_id']


from customer.serializers import CustomerInvoiceSerializer
class ConnectionInvoiceSerializer(serializers.ModelSerializer):
    customer = CustomerInvoiceSerializer(many=False)
    subarea = SubAreaSerializer(many=False)
    package = ProductSerializer(read_only=True)
    expiry_date = serializers.DateField(read_only=True)
    subscription_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Connection
        fields = ['id', 'connection_id', 'installation_date',
                  'subarea', 'package', 'status', 'new', 'customer', 'expiry_date','subscription_id']
