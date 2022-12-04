from rest_framework import serializers
from .models import Country, City, Area, SubArea

# for Create, Update & Delete operations
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'


# For use in related serializer class only
class CitySerializerForArea(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city', 'country']

class AreaSerializerForSubArea(serializers.ModelSerializer):
    city = CitySerializerForArea(read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'area', 'city']


# For Read Operation
class CitySerializerRelated(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    areas = AreaSerializer(many=True)

    class Meta:
        model = City
        fields = ['id', 'city', 'areas', 'country']


class AreaSerializerRelated(serializers.ModelSerializer):
    city = CitySerializerForArea(read_only=True)
    subareas = SubAreaSerializer(many=True)

    class Meta:
        model = Area
        fields = ['id', 'area', 'subareas', 'city']

class SubAreaSerializerRelated(serializers.ModelSerializer):
    area = AreaSerializerForSubArea(read_only=True)

    class Meta:
        model = SubArea
        fields = ['id', 'subarea', 'area']