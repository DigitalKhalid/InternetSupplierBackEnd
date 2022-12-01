from rest_framework import serializers
from .models import Country, City, Area, SubArea

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = ['id', 'subarea']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CitySerializerRelated(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    areas = AreaSerializer(many=True)

    class Meta:
        model = City
        fields = ['id', 'city', 'areas', 'country']

class CitySerializerForArea(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city', 'country']

class AreaSerializerRelated(serializers.ModelSerializer):
    city = CitySerializerForArea(read_only=True)
    subareas = SubAreaSerializer(many=True)

    class Meta:
        model = Area
        fields = ['id', 'area', 'subareas', 'city']

class LocationSerializer(serializers.ModelSerializer):
    cities = CitySerializerRelated(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country', 'cities']

