from django.contrib import admin

# Register your models here.
from .models import Region, Location, Transport, Food, Route, Hotel, Contact

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'distance_air', 'picture']

class TransportAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity_place', 'price']
    
class RouteAdmin(admin.ModelAdmin):
    list_display = ['time', 'num_tran', 'description', 'check_tur', 'kind_tran', 'location']
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ['kitchen', 'description', 'price_day', 'check_tur', 'location']
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'mobile', 'telegram', 'home']
    search_fields = ['user', 'name', 'email', 'mobile', 'telegram', 'home']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'pic_cart', 'price', 'check_tur', 'contact', 'location']


admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Hotel, HotelAdmin)

