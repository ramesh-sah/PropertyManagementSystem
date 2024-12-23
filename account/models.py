from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from account.manager import UserManager


class User(AbstractBaseUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('customer', 'Customer'),
    ]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True,max_length=255, blank=False, null=False)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    
    
    
    
    


class UserSocialMediaProfile(models.Model):
    SOCIAL_MEDIA_PLATFORMS = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('WhatsApp', 'WhatsApp'),
    ]

    social_media_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media_profiles')
    platform = models.CharField(max_length=30, choices=SOCIAL_MEDIA_PLATFORMS)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} profile of {self.user.username}"

        
        

class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}"