
from django.urls import path

from account.views import  AgentProfileView, CustomerProfileView, UserDashboard, UserLogin,UserRegistration,AgentDashboard,AdminDashboard,AdminAddAgentView,AdminListAgentView,AdminDetailAgentView,AdminAddCustomerView,AdminListCustomerView,AdminDetailCustomerView,AdminProfileView


app_name='account'
urlpatterns = [

    path('register/',UserRegistration.as_view(),name='user-register'),
    path('login/',UserLogin.as_view(),name='user-login'),

    path('admin-dashboard/',AdminDashboard.as_view(),name='admin-dashboard'),
    path('admin-add-agent/',AdminAddAgentView.as_view(),name='admin-add-agent'),
    path('admin-list-agent/',AdminListAgentView.as_view(),name='admin-list-agent'),
    path('admin-detail-agent/',AdminDetailAgentView.as_view(),name='admin-detail-agent'),
    path('admin-add-customer/',AdminAddCustomerView.as_view(),name='admin-add-customer'),
    path('admin-list-customer/',AdminListCustomerView.as_view(),name='admin-list-customer'),
    path('admin-detail-customer/',AdminDetailCustomerView.as_view(),name='admin-detail-customer'),
    path('admin-profile/',AdminProfileView.as_view(),name='admin-profile'),

    path('agent-dashboard/',AgentDashboard.as_view(),name='agent-dashboard'),
    path('agent-profile/',AgentProfileView.as_view(),name='agent-profile'),

    path('dashboard/',UserDashboard.as_view(),name='user-dashboard'),
    path('customer-profile/',CustomerProfileView.as_view(),name='customer-profile'),



]
