from rest_framework import serializers
from .models import Order, OrderDetail, OrderPackageDetail
from connection.serializers import ConnectionSerializer, ConnectionSerializerRelated
from product.serializers import ProductSerializerRelated

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderPackageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPackageDetail
        fields = '__all__'

class OrderDetailSerializerRelated(serializers.ModelSerializer):
    product = ProductSerializerRelated(read_only=True, many=False)
    packagedetails = OrderPackageDetailSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'

from connection.serializers import ConnectionInvoiceSerializer
class OrderInvoiceSerializer(serializers.ModelSerializer):
    connection = ConnectionInvoiceSerializer(read_only=True)
    details = OrderDetailSerializerRelated(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'date_created', 'connection', 'status', 'details']

from payment.serializers import PaymentSerializer
class OrderSerializerRelated(serializers.ModelSerializer):
    connection = ConnectionSerializer(read_only=True)
    details = OrderDetailSerializerRelated(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    payment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'date_created', 'connection', 'status', 'details', 'payments', 'payment_count']


# Invoice
class InvoiceSerializer(serializers.ModelSerializer):
    connection = ConnectionInvoiceSerializer(read_only=True)
    details = OrderDetailSerializerRelated(many=True, read_only=True)
    payment_count = serializers.IntegerField(read_only=True)
    payment_received = serializers.IntegerField(read_only=True)
    # value = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'date_created', 'connection', 'status', 'details', 'payment_count', 'payment_received']
