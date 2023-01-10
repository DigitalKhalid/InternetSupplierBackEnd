from rest_framework import serializers
from .models import Payment
from django.db.models import Sum, Q
from django.db.models.functions import ExtractMonth, ExtractYear, TruncMonth
from datetime import date

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentHistoryDashboardSerializer(serializers.ModelSerializer):
    payment_month = serializers.DateField()
    total_amount = serializers.IntegerField()

    class Meta:
        model = Payment
        fields = ['payment_month', 'total_amount']

    # def get_payment_month(self, obj):
    #     paymentmonth = Payment.objects.all().aggregate(payment_month=TruncMonth('date_created').values('month'))
    #     return paymentmonth["payment_month"]

class PaymentDashboardSerializer(serializers.ModelSerializer):
    payment_today = serializers.SerializerMethodField()
    payment_this_month = serializers.SerializerMethodField()
    payment_this_year = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ['payment_today', 'payment_this_month', 'payment_this_year']

    def get_payment_today(self, obj):
        paymenttoday = Payment.objects.all().aggregate(payment_today=Sum('amount', filter=Q(date_created__startswith = date.today())))
        return paymenttoday["payment_today"]

    def get_payment_this_month(self, obj):
        today = date.today()
        paymentthistoday = Payment.objects.all().aggregate(payment_this_month=Sum('amount', filter=Q(date_created__gte = date(today.year, today.month, 1)) & Q(date_created__lte = date(today.year, today.month, 31))))
        return paymentthistoday["payment_this_month"]

    def get_payment_this_year(self, obj):
        today = date.today()
        paymentthisyear = Payment.objects.all().aggregate(payment_this_year=Sum('amount', filter=Q(date_created__gte = date(today.year, 1, 1)) & Q(date_created__lte = date(today.year, 12, 31))))
        return paymentthisyear["payment_this_year"]

from order.serializers import OrderSerializer, OrderInvoiceSerializer

class PaymentSerializerRelated(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    cashier_name = serializers.CharField(read_only=True)
    connection_id = serializers.CharField(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'date_created', 'payment_type', 'order', 'cashier_name', 'amount', 'received_by', 'connection_id']

class PaymentInvoiceSerializer(serializers.ModelSerializer):
    order = OrderInvoiceSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'