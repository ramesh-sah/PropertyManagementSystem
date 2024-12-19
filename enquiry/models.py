from django.db import models

# Create your models here.
class Enquiry(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
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