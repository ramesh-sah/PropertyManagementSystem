from django.contrib import admin

from contact_us.models import ContactUs

# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
   
    def mark_as_read(self, request, queryset):
        """
        Custom admin action to mark selected enquiries as read.
        """
        queryset.update(status='read')

    def mark_as_unread(self, request, queryset):
        """
        Custom admin action to mark selected enquiries as unread.
        """
        queryset.update(status='unread')

    mark_as_read.short_description = 'Mark selected enquiries as read'
    mark_as_unread.short_description = 'Mark selected enquiries as unread'
