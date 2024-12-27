from django.shortcuts import render
from django.views import View

# Create your views here.

    
class AdminContactListView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'admin/contact_us/contact-us.html')
    
    
    
class AgentContactView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'agent/contact_us/contact-us.html')
    
    
class CustomerContactView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        """
       
        return render(request, 'customer/contact_us/contact-us.html')