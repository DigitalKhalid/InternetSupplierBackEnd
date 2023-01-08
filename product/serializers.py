from rest_framework import serializers
from .models import Product, ProductType, ProductCatagory, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductCatagorySerializer(serializers.ModelSerializer):
    type = ProductTypeSerializer(read_only=True)

    class Meta:
        model = ProductCatagory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerRelated(serializers.ModelSerializer):
    # type = ProductTypeSerializer(read_only=True)
    catagory = ProductCatagorySerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'catagory', 'title', 'sku', 'description', 'unit', 'purchase_price', 'sale_price', 'date_created']

class PackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'sale_price']


class ProductListSerializer(serializers.ModelSerializer):
    product_type = serializers.CharField()
    catagory_title = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'sale_price', 'sku', 'product_type', 'catagory_title']
