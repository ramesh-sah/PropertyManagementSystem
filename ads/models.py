from datetime import timezone
from django.db import models

# Create your models here.

class Ads(models.Model):
    ad_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=200, help_text="Title of the ad")
    description = models.TextField(help_text="Detailed description of the ad")
    image = models.ImageField(upload_to='ads/images/', blank=True, null=True, help_text="Upload an image representing the ad")
    url = models.URLField(help_text="URL for the ad's landing page")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date when the ad was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date when the ad was last updated")
    status = models.CharField(max_length=20, default='Active', help_text="Status of the ad (e.g., Active, Inactive)")
    start_date = models.DateTimeField(help_text="Date when the ad starts displaying")
    end_date = models.DateTimeField(help_text="Date when the ad stops displaying")

    def save(self, *args, **kwargs):
        # Automatically update status based on end_date before saving
        if self.end_date < timezone.now():
            self.status = 'Inactive'
        super().save(*args, **kwargs)

    @classmethod
    def update_ad_status(cls):
        # Update status for all ads based on their end date
        current_time = timezone.now()
        cls.objects.filter(end_date__lt=current_time, status='Active').update(status='Inactive')

    def __str__(self):
        return f"Ad: {self.title} (ID: {self.ad_id})"