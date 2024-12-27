from django.urls import path

from property.views import AdminPropertyAddView,AdminPropertyListView,AdminPropertyEnquiryView,AdminPropertyDetailView,AdminPropertyCouponAddView,AdminPropertyCouponListView,AdminPropertyCouponUpdateView, AgentPropertyAddView, AgentPropertyCouponAddView, AgentPropertyCouponListView, AgentPropertyCouponUpdateView, AgentPropertyDetailView, AgentPropertyEnquiryView, AgentPropertyListView, CustomerPropertyDetailView, CustomerPropertyEnquiryView, CustomerPropertyListView
app_name='property'
urlpatterns = [
  

    path('admin/add-property/',AdminPropertyAddView.as_view(), name='admin-add-property'),
    path('admin/list-property/',AdminPropertyListView.as_view(), name='admin-list-property'),
    path('admin/enquiry-property/',AdminPropertyEnquiryView.as_view(), name='admin-enquiry-property'),
    path('admin/detail-property/',AdminPropertyDetailView.as_view(), name='admin-detail-property'),
    path('admin/add-property-coupon/',AdminPropertyCouponAddView.as_view(), name='admin-property-coupon-add'),
    path('admin/list-property-coupon/',AdminPropertyCouponListView.as_view(), name='admin-property-coupon-list'),
    path('admin/update-property-coupon/',AdminPropertyCouponUpdateView.as_view(), name='admin-property-coupon-update'),
    
    
    path('agent/add-property/',AgentPropertyAddView.as_view(), name='agent-add-property'),
    path('agent/list-property/',AgentPropertyListView.as_view(), name='agent-list-property'),
    path('agent/enquiry-property/',AgentPropertyEnquiryView.as_view(), name='agent-enquiry-property'),
    path('agent/detail-property/',AgentPropertyDetailView.as_view(), name='agent-detail-property'),
    path('agent/add-property-coupon/',AgentPropertyCouponAddView.as_view(), name='agent-property-coupon-add'),
    path('agent/list-property-coupon/',AgentPropertyCouponListView.as_view(), name='agent-property-coupon-list'),
    path('agent/update-property-coupon/',AgentPropertyCouponUpdateView.as_view(), name='agent-property-coupon-update'),
    
    
    path('customer/list-property/',CustomerPropertyListView.as_view(), name='customer-list-property'),
    path('customer/detail-property/',CustomerPropertyDetailView.as_view(), name='customer-detail-property'),
    path('customer/enquiry-property/',CustomerPropertyEnquiryView.as_view(), name='customer-enquiry-property'),


]