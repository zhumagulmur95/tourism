from django.contrib.auth.models import User
from accounts.models import userProfile
from accounts.permissions import IsOwnerProfileOrReadOnly
from rest_framework import viewsets

from .models import Region, Location, Tours, Contact, Hotel, Food, Transport, Route
from .serializers import RegionSerializer, LocationSerializer, ToursSerializer, ContactSerializer, HotelSerializer, FoodSerializer, TransportSerializer, RouteSerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)


class ToursViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)


class TransportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]  

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)  
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)





