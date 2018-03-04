from django.contrib import admin

from .models import Park, AmenityType, ParkAmenity


class ParkAmenityTabularInline(admin.TabularInline):
    model = ParkAmenity


class ParkAdmin(admin.ModelAdmin):
    model = Park
    inlines = [ParkAmenityTabularInline]


class AmenityTypeAdmin(admin.ModelAdmin):
    model = AmenityType


admin.site.register(Park, ParkAdmin)
admin.site.register(AmenityType, AmenityTypeAdmin)
