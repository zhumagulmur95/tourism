from rest_framework import viewsets
from .models import Region, Location, Contact, Hotel, Food, Transport, Route
from .serializers import RegionSerializer, LocationSerializer, ContactSerializer, HotelSerializer, FoodSerializer, TransportSerializer, RouteSerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TransportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer    
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer





