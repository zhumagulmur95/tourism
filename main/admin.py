from django.contrib import admin

# Register your models here.
from .models import Region, Location, Tours, Transport, Food, Route, Hotel, Contact

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'picture']
    search_fields = ['user', 'name']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'distance_air', 'picture', 'description']

class ToursAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'picture', 'location']
    search_fields = ['user', 'name', 'price']

class TransportAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity_place', 'price']
    search_fields = ['user', 'name', 'price']
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'num_tran', 'description', 'check_tur', 'kind_tran', 'location']
    search_fields = ['user', 'time', 'num_tran']
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'kitchen', 'description', 'price_day', 'check_tur', 'picture', 'location']
    search_fields = ['user', 'kitchen']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'mobile', 'telegram', 'home']
    search_fields = ['user', 'name', 'email', 'mobile', 'telegram', 'home']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'adress', 'pic_cart', 'price', 'check_tur', 'contact', 'location']
    search_fields = ['user', 'name', 'adress', 'price']


admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tours, ToursAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Hotel, HotelAdmin)

