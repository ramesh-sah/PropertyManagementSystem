from django.contrib import admin
from .models import User,UserSocialMediaProfile,UserAddress
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   
    pass

@admin.register(UserSocialMediaProfile)
class UserSocialMediaAdmin(admin.ModelAdmin):
   
    pass


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
   
    pass