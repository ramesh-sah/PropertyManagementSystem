from django.urls import path

from property.views import AdminAddPropertyView

urlpatterns = [
  
    # path('customer/about/', CustomerAboutOrganizationView.as_view(), name='about_organization'),
    path('admin/add-property/',AdminAddPropertyView.as_view(), name='admin-add-property'),
    # path('agent/about/', AdminAboutOrganizationView.as_view(), name='about_organization'),
    

]