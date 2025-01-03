from django.contrib import admin

# Register your models here.
from .models import PropertyAmenities, Property


@admin.register(PropertyAmenities)
class PropertyAmenitiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Property)
