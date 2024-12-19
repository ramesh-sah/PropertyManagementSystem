from django.db import models

# Create your models here.

class OrganizationDetails(models.Model):
    organization_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload the organization logo")
    name = models.CharField(max_length=255, help_text="Name of the organization")
    description = models.TextField(blank=True, null=True, help_text="Description of the organization")
    established_date = models.DateField(blank=True, null=True, help_text="Date the organization was established")
    website = models.URLField(blank=True, null=True, help_text="Website URL of the organization")
    phone_number = models.CharField(max_length=15, blank=True, help_text="Contact phone number for the organization")
    email = models.EmailField(blank=True, null=True, help_text="Contact email address for the organization")
    address = models.CharField(max_length=255, blank=True, null=True, help_text="Physical address of the organization")
    mission_statement = models.TextField(blank=True, null=True, help_text="Mission statement of the organization")
    vision_statement = models.TextField(blank=True, null=True, help_text="Vision statement of the organization")
    industry = models.CharField(max_length=100, blank=True, null=True, help_text="Industry in which the organization operates")

    def __str__(self):
        return self.name
    
    

class OrganizationRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Name of the role")
    description = models.TextField(blank=True, null=True, help_text="Description of the role")

    def __str__(self):
        return self.name
    



class OrganizationTeamMember(models.Model):
    team_member_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_member')
    organization_id = models.ForeignKey('OrganizationDetails', on_delete=models.CASCADE, related_name='team_members')
    role_id = models.ForeignKey('OrganizationRole', on_delete=models.CASCADE, related_name='members')
    bio = models.TextField(blank=True, null=True, help_text="Short biography of the team member")
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True, help_text="Upload member photo")
    start_date = models.DateField(blank=True, null=True, help_text="Date the team member started with the organization")
    end_date = models.DateField(blank=True, null=True, help_text="Date the team member left the organization")
    linked_in_profile = models.URLField(blank=True, null=True, help_text="LinkedIn profile URL of the team member")
    phone_number = models.CharField(max_length=15, blank=True, help_text="Contact phone number for the team member")
    whatsapp_number = models.CharField(max_length=15, blank=True, help_text="WhatsApp contact number for the team member")
    instagram_username = models.CharField(max_length=100, blank=True, help_text="Instagram username of the team member")
    facebook_profile_url = models.URLField(blank=True, null=True, help_text="Facebook profile URL of the team member")

    def __str__(self):
        return f"{self.user_id.username} - {self.role_id.name}"
    
    
    
class OrganizationSocialMedia(models.Model):
    org_social_media_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media_links')
    organization_id = models.ForeignKey('OrganizationDetails', on_delete=models.CASCADE, related_name='social_media_links')
    platform = models.CharField(max_length=50, help_text="Name of the social media platform")
    url = models.URLField(help_text="URL of the social media profile")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date the link was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date the link was last updated")

    def __str__(self):
        return f"{self.platform} profile of {self.organization_id.name}"
    
class AboutOrganization(models.Model):
    about_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about_organizations')
    organization_id = models.ForeignKey('OrganizationDetails', on_delete=models.CASCADE, related_name='about_organizations')
    overview = models.TextField(blank=True, null=True, help_text="Brief overview of the organization")
    history = models.TextField(blank=True, null=True, help_text="Historical background of the organization")
    core_values = models.TextField(blank=True, null=True, help_text="Core values of the organization")
    achievements = models.TextField(blank=True, null=True, help_text="Notable achievements of the organization")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date when the about section was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date when the about section was last updated")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload an image representing the organization")
    banner_image = models.ImageField(upload_to='banners/', blank=True, null=True, help_text="Upload a banner image for the about section")

    def __str__(self):
        return f"About Info for {self.organization_id.name} (ID: {self.about_id})"
    
    

class OrganizationTermsAndConditions(models.Model):
    terms_id = models.AutoField(primary_key=True)
    organization_id = models.ForeignKey('OrganizationDetails', on_delete=models.CASCADE, related_name='terms_conditions')
    content = models.TextField(blank=True, null=True, help_text="Content of the terms and conditions")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date when the terms were created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date when the terms were last updated")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='terms_conditions')

    def __str__(self):
        return f"Terms for {self.organization_id.name} (ID: {self.terms_id})"