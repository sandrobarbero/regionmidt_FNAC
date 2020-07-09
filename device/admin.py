from django.contrib import admin
from .models import UserProfile, Device, Location, Category


class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class LocationAdmin(admin.ModelAdmin):
    search_fields = ('building', 'address',)
    list_display = ('building', 'address',)

admin.site.register(UserProfile)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)
