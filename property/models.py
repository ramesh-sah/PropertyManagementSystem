from django.db import models

from account.models import User
    
from django.db import models
from django.utils.timezone import now
from datetime import timedelta

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
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('liked', 'Liked'),
    ]

    property_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', limit_choices_to={'user_type': 'agent','user_type': 'admin'})
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
    image = models.ImageField(upload_to='images/', help_text="Upload an image" ,null=True, blank=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True, help_text="Upload a video",)
    video_title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for the video")

    def __str__(self):
        return f"{self.image_title or self.video_title} for {self.property.title}"



class PropertyAmenities(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities')
    amenities_status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ac = models.BooleanField(default=False, help_text="A/C available")
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
    elevator = models.BooleanField(default=False, help_text="Elevator available")
    

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
    
    

# Create your models here.
class PropertyEnquiry(models.Model):
    property_enquiry_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_enquiry")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_property_enquiry')
    name = models.CharField(max_length=100, help_text="Name of the person making the enquiry")
    email = models.EmailField(help_text="Email address of the person making the enquiry")
    phone = models.CharField(max_length=15, blank=True, help_text="Contact phone number for the person")
    subject = models.CharField(max_length=150, help_text="Subject of the enquiry")
    message = models.TextField(help_text="Detailed message of the enquiry")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date when the enquiry was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date when the enquiry was last updated")
    status = models.CharField(max_length=20, default='Pending', help_text="Status of the enquiry (e.g., Pending, Responded)")

    def __str__(self):
        return f"Enquiry from {self.name} (ID: {self.enquiry_id})"
    
    
    
    

class PropertyCoupon(models.Model):
    """Model representing a discount coupon for a property."""
    COUPON_TYPE_CHOICES = [
        ('FLAT', 'Flat Discount'),
        ('PERCENT', 'Percentage Discount'),
        ('BOGO', 'Buy One Get One Free'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="coupons")
    code = models.CharField(max_length=20, unique=True)  # Unique coupon code
    coupon_type = models.CharField(max_length=10, choices=COUPON_TYPE_CHOICES, default='FLAT')
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valid_from = models.DateTimeField(default=now)
    valid_until = models.DateTimeField(default= now() + timedelta(days=30))  # Default validity: 30 days
    max_uses = models.PositiveIntegerField(default=1)  # Maximum times the coupon can be used
    uses = models.PositiveIntegerField(default=0)  # Tracks how many times the coupon has been used
    is_active = models.BooleanField(default=True)

    def apply_discount(self, total_amount, item_count=1):
        """
        Apply the discount to the total amount.
        - Returns the discounted total.
        - Raises an exception if the coupon is invalid or expired.
        """
        if not self.is_valid():
            raise ValueError("Coupon is not valid or expired.")

        if self.coupon_type == 'PERCENT' and self.discount_percentage:
            discount = total_amount * (self.discount_percentage / 100)
        elif self.coupon_type == 'FLAT' and self.discount_amount:
            discount = min(self.discount_amount, total_amount)
        elif self.coupon_type == 'BOGO':
            # BOGO applies when at least 2 items are purchased
            if item_count >= 2:
                discount = total_amount / item_count  # Discount the price of one item
            else:
                discount = 0
        else:
            discount = 0

        return max(total_amount - discount, 0)

    def is_valid(self):
        """
        Check if the coupon is valid.
        - Active
        - Within the validity period
        - Not exceeding max uses
        """
        return (
            self.is_active and
            self.valid_from <= now() <= self.valid_until and
            self.uses < self.max_uses
        )

    def use_coupon(self):
        """
        Increment the usage count of the coupon.
        Deactivate the coupon if max uses is reached.
        """
        if not self.is_valid():
            raise ValueError("Cannot use an invalid or expired coupon.")

        self.uses += 1
        if self.uses >= self.max_uses:
            self.is_active = False
        self.save()

    def is_nearing_expiration(self, days=5):
        """
        Check if the coupon is nearing its expiration date.
        - Returns True if within the specified number of days from expiration.
        """
        return self.valid_until <= now() + timedelta(days=days)

    def __str__(self):
        return f"Coupon {self.code} for {self.property.name}"

    @classmethod
    def create_coupon(cls, property, code, discount_amount=None, discount_percentage=None, max_uses=1):
        """
        Create a new coupon with validation.
        - Ensures that at least one type of discount is provided.
        """
        if discount_amount is None and discount_percentage is None:
            raise ValueError("At least one discount type must be provided.")

        coupon = cls(property=property, code=code, discount_amount=discount_amount,
                     discount_percentage=discount_percentage, max_uses=max_uses)
        coupon.save()
        return coupon