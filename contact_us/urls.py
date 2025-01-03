
from django.urls import path

from .views import AdminContactListView, AgentContactView, CustomerContactView

app_name='contact_us'
urlpatterns = [
    
    path('admin-contact-list/',AdminContactListView.as_view(),name='admin-contact-list'),
    path('admin-contact-update/<int:contact_us_id>/',AdminContactListView.as_view(),name='admin-contact-update'),
    path('agent-contact/',AgentContactView.as_view(),name='agent-contact'),
    path('customer-contact/',CustomerContactView.as_view(),name='customer-contact'),

    
]
