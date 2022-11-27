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
    subareas = SubAreaSerializer(many=True)

    class Meta:
        model = Area
        fields = ['id', 'area', 'subareas']

class CitySerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True)

    class Meta:
        model = City
        fields = ['id', 'city', 'areas']

class LocationSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country', 'cities']

