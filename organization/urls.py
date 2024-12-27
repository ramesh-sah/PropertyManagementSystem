from django.urls import path

from organization.views import  AdminOrganizationRoleView,AdminOrganizationDetailView,AdminOrganizationSocialMedia,AdminOrganizationTeamMember,AdminOrganizationTermsConditionView,AdminAboutOrganizationView, AgentAboutOrganizationView, AgentOrganizationTermsConditionView, CustomerAboutOrganizationView, CustomerOrganizationTermsConditionView

app_name='organization'

urlpatterns = [
  
    # path('customer/about/', CustomerAboutOrganizationView.as_view(), name='about_organization'),
    # path('admin/about/', AdminAboutOrganizationView.as_view(), name='about_organization'),
    # path('agent/about/', AdminAboutOrganizationView.as_view(), name='about_organization'),
    path('admin/organization-role/', AdminOrganizationRoleView.as_view(), name='organization-role'),
    path('admin/organization-detail/', AdminOrganizationDetailView.as_view(), name='organization-detail'),
    path('admin/organization-social-media/', AdminOrganizationSocialMedia.as_view(), name='organization-social-media'),
    path('admin/organization-team-member/', AdminOrganizationTeamMember.as_view(), name='organization-team-member'),
    path('admin/organization-terms-condition/', AdminOrganizationTermsConditionView.as_view(), name='organization-terms-condition'),
    path('admin/about-organization/', AdminAboutOrganizationView.as_view(), name='about-organization'),
    
    path('agent/organization-terms-condition/', AgentOrganizationTermsConditionView.as_view(), name='agent-organization-terms-condition'),
    
    path('agent/about-us/', AgentAboutOrganizationView.as_view(), name='agent-about-us'),
    
    
    
    path('customer/organization-terms-condition/', CustomerOrganizationTermsConditionView.as_view(), name='customer-organization-terms-condition'),
    
    path('customer/about-us/', CustomerAboutOrganizationView.as_view(), name='customer-about-us'),
    
    

]