from rest_framework import serializers
from .models import Customer
from location.serializers import SubAreaSerializerRelated

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerSerializerRelated(serializers.ModelSerializer):
    subarea = SubAreaSerializerRelated(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'