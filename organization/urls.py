from django.urls import path

from organization.views import  AdminAboutOrganizationView, CustomerAboutOrganizationView


urlpatterns = [
  
    path('customer/about/', CustomerAboutOrganizationView.as_view(), name='about_organization'),
    path('admin/about/', AdminAboutOrganizationView.as_view(), name='about_organization'),
    path('agent/about/', AdminAboutOrganizationView.as_view(), name='about_organization'),
    

]