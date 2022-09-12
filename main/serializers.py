from dataclasses import fields
from rest_framework import serializers

from .models import Region, Location, Tours, Contact, Hotel, Food, Transport, Route

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'picture']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'distance_air', 'picture', 'description', 'region']

class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'price', 'description', 'picture', 'location']

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name', 'quantity_place', 'price']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'time', 'num_tran', 'description', 'kind_tran', 'location']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'kitchen', 'description', 'price_day', 'picture', 'location']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'mobile', 'telegram', 'home']
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'adress', 'pic_cart', 'price', 'contact', 'location']