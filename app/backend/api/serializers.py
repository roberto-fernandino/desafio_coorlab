from rest_framework import serializers
from .models import Trip, City


class TripSerializer(serializers.ModelSerializer):

    city_name = serializers.SerializerMethodField()
    
    def get_city_name(self, obj):
        return obj.city.name if obj.city else None
    
    class Meta:
        model = Trip
        fields = [
            'id',
            'name',
            'price_confort',
            "price_econ",
            "city_name",
            "duration",
            "seat",
            "bed",
        ]


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
        ]
