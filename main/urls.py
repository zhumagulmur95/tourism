from .views import RegionViewSet, LocationViewSet, ContactViewSet, HotelViewSet, FoodViewSet, TransportViewSet, RouteViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'region/', RegionViewSet, basename='region')
router.register(r'location/', LocationViewSet, basename='location')
router.register(r'transport/', TransportViewSet, basename='transport')
router.register(r'route/', RouteViewSet, basename='route')
router.register(r'food/', FoodViewSet, basename='food')
router.register(r'contact/', ContactViewSet, basename='contact')
router.register(r'hotel/', HotelViewSet, basename='hotel')

urlpatterns = router.urls
