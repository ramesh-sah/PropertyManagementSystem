from django.contrib import admin

# Register your models here.
from .models import PropertyAmenities, Property, PropertyListingDetail,PropertyMedia,PropertyAddress


@admin.register(PropertyAmenities)
class PropertyAmenitiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Property)
admin.site.register(PropertyListingDetail)
admin.site.register(PropertyMedia)
admin.site.register(PropertyAddress)
