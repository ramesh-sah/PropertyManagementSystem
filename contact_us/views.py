from django.shortcuts import render
from django.views import View
from django.core.exceptions import PermissionDenied

from propertymanagement.permisssions import IsAdminUser, IsAgentUser, IsCustomerUser

# Create your views here.

    
class AdminContactListView(View):
    permission_class=IsAdminUser()
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'admin/contact_us/contact-us.html')
    
    
    
class AgentContactView(View):
    permission_class=IsAgentUser()
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'agent/contact_us/contact-us.html')
    
    
class CustomerContactView(View):
    permission_class=IsCustomerUser()
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'customer/contact_us/contact-us.html')