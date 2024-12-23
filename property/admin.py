from django.contrib import admin

# Register your models here.
from .models import PropertyAmenities

@admin.register(PropertyAmenities)
class PropertyAmenitiesAdmin(admin.ModelAdmin):
   
    pass