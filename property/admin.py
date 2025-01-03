from django.contrib import admin

# Register your models here.
from .models import PropertyAmenities,Property,PropertyListingDetail,PropertyAddress,PropertyCoupon,PropertyEnquiry,PropertyMedia
@admin.register(PropertyAmenities)
class PropertyAmenitiesAdmin(admin.ModelAdmin):
   
    pass



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
   
    pass

@admin.register(PropertyListingDetail)
class PropertyListingDetailAdmin(admin.ModelAdmin):
   
    pass


@admin.register(PropertyAddress)
class PropertyAddressAdmin(admin.ModelAdmin):
   
    pass
@admin.register(PropertyMedia)
class PropertyMediaAdmin(admin.ModelAdmin):
   
    pass


@admin.register(PropertyCoupon)
class PropertyCoupon(admin.ModelAdmin):
   
    pass


@admin.register(PropertyEnquiry)
class PropertyEnquiryAdmin(admin.ModelAdmin):
   
    pass