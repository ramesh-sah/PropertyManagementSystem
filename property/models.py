from django.db import models

from account.models import User

# Create your models here.



class Property(models.Model):
    PROPERTY_CATEGORIES = [
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('house', 'House'),
        ('industrial', 'Industrial'),
        ('villa', 'Villa'),
    ]

    LISTING_STATUSES = [
        ('for sale', 'For Sale'),
        ('for rent', 'For Rent'),
    ]

    property_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', limit_choices_to={'user_type': 'agent'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=PROPERTY_CATEGORIES)
    status = models.CharField(max_length=10, choices=LISTING_STATUSES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    

class PropertyListingDetail(models.Model):
    listing_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='listing_details')
    size = models.IntegerField(help_text="Size in square feet")
    bedrooms = models.IntegerField(help_text="Number of bedrooms")
    kitchens = models.IntegerField(help_text="Number of kitchens")
    store_rooms = models.IntegerField(help_text="Number of store rooms")
    halls = models.IntegerField(help_text="Number of halls")
    floors_no = models.IntegerField(help_text="Number of floors")

    def __str__(self):
        return f"Listing Details for {self.property.title}"
    
    
    
class PropertyMedia(models.Model):
    media_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='media')
    image_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for the image")
    image_url = models.URLField(help_text="URL for the image")
    video_upload = models.URLField(blank=True, null=True, help_text="URL for the uploaded video")
    video_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for the video")

    def __str__(self):
        return f"{self.image_title or self.video_title} for {self.property.title}"



class PropertyAmenities(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities')
    amenities_title=models.DateField(max_length=255)
    amenities_description=models.TextField()
    amenities_status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    """ ac = models.BooleanField(default=False, help_text="A/C available")
    heating = models.BooleanField(default=False, help_text="Heating available")
    garage = models.BooleanField(default=False, help_text="Garage available")
    swimming_pool = models.BooleanField(default=False, help_text="Swimming pool available")
    parking = models.BooleanField(default=False, help_text="Parking available")
    lake_view = models.BooleanField(default=False, help_text="Lake view available")
    garden = models.BooleanField(default=False, help_text="Garden available")
    disabled_access = models.BooleanField(default=False, help_text="Disabled access available")
    lift = models.BooleanField(default=False, help_text="Lift available")
    pet_friendly = models.BooleanField(default=False, help_text="Pet friendly")
    ceiling_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Ceiling height in feet")
    outdoor_shower = models.BooleanField(default=False, help_text="Outdoor shower available")
    refrigerator = models.BooleanField(default=False, help_text="Refrigerator available")
    wifi = models.BooleanField(default=False, help_text="Wi-Fi available")
    tv_cable = models.BooleanField(default=False, help_text="Cable TV available")
    barbecue = models.BooleanField(default=False, help_text="Barbecue available")
    laundry_dryer = models.BooleanField(default=False, help_text="Laundry dryer available")
    lawn = models.BooleanField(default=False, help_text="Lawn available")
    elevator = models.BooleanField(default=False, help_text="Elevator available")"""
    

    def __str__(self):
        return f"Amenities for {self.property.title}"
    
    
    

class PropertyAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255, help_text="Street address")
    country = models.CharField(max_length=100, help_text="Country name")
    city = models.CharField(max_length=100, help_text="City name")
    zip_code = models.CharField(max_length=20, help_text="Zip code")
    state = models.CharField(max_length=100, help_text="State name")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text="Latitude for location")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text="Longitude for location")

    def __str__(self):
        return f"Address for {self.property.title}: {self.address}, {self.city}, {self.state}, {self.country}"
    

