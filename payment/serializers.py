from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


from order.serializers import OrderSerializer, OrderInvoiceSerializer

class PaymentSerializerRelated(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    cashier_name = serializers.CharField(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'date_created', 'payment_type', 'order', 'cashier_name', 'amount', 'received_by']

class PaymentInvoiceSerializer(serializers.ModelSerializer):
    order = OrderInvoiceSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'