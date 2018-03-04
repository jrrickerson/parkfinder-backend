from django.contrib import admin

from .models import Park, AmenityType, ParkAmenity


class ParkAmenityTabularInline(admin.TabularInline):
    model = ParkAmenity
    extra = 1
    verbose_name_plural = 'park amenities'


class ParkAdmin(admin.ModelAdmin):
    model = Park
    inlines = [ParkAmenityTabularInline]
    list_display = (
        'name',
        'address',
        'zipcode',
        'county',
        'district',
    )
    list_display_filter = (
        'country',
        'district',
        'zipcode',
    )
    search_fields = (
        'name',
        'former_name',
        'notes',
        'amenities__description',
    )


class AmenityTypeAdmin(admin.ModelAdmin):
    model = AmenityType


admin.site.register(Park, ParkAdmin)
admin.site.register(AmenityType, AmenityTypeAdmin)
