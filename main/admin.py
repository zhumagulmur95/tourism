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
    list_display = ['time', 'num_tran', 'description', 'chek_tur', 'kind_tran', 'location']
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ['kitchen', 'description', 'price_day', 'chek_tur', 'location']
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'telegram', 'home']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'pic_card', 'price', 'check_tur', 'contact', 'location']


admin.site.register(Region)
admin.site.register(Location)
admin.site.register(Transport)
admin.site.register(Route)
admin.site.register(Food)
admin.site.register(Contact)
admin.site.register(Hotel)

