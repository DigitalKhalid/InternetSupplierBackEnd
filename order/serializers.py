from rest_framework import serializers
from .models import Order, OrderDetail
from connection.serializers import ConnectionSerializer
from product.serializers import ProductSerializerRelated

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderDetailSerializerRelated(serializers.ModelSerializer):
    product = ProductSerializerRelated(read_only=True, many=False)

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializerRelated(serializers.ModelSerializer):
    connection = ConnectionSerializer(read_only=True)
    details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'date_created', 'connection', 'value', 'status', 'details']
