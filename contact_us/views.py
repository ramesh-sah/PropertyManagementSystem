from django.shortcuts import redirect, render
from django.views import View
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from contact_us.models import ContactUs
from propertymanagement.permisssions import IsAdminUser, IsAgentUser, IsCustomerUser
from django.contrib  import messages

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
        Handles GET requests to display a list of enquiries.
        """
        enquiries = ContactUs.objects.all().order_by('-created_at')
        paginator = Paginator(enquiries, 10)  # Show 10 enquiries per page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'admin/contact_us/contact-us.html', {'enquiries': page_obj})
    
    
    def post(self, request, contact_us_id):
        """
        Handles POST requests to update the status of an enquiry.
        """
        enquiry = ContactUs.objects.get(contact_us_id=contact_us_id)
        new_status = request.POST.get('status')  # Get status from POST data
        enquiry.status = new_status
        enquiry.save()

        return redirect('contact_us:admin-contact-list')  # Redirect to the list view
    
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
    def post(self, request, *args, **kwargs):
        message=request.POST.get('message')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        phone=request.POST.get('phone') 
        
        try:
            ContactUs.objects.create(name=name,message=message,email=email,subject=subject,phone=phone)    
            messages.success(request,"Enquiry Submited Successful ") 
            return redirect('property:agent-list-property') 
        except:
            messages.warning(request,"Recheck the Required Fields and Try Again")
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
    
    def post(self, request, *args, **kwargs):
        message=request.POST.get('message')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        phone=request.POST.get('phone') 
        
        try:
            ContactUs.objects.create(name=name,message=message,email=email,subject=subject,phone=phone)    
            messages.success(request,"Enquiry Submited Successful ") 
            return redirect('property:customer-list-property') 
        except:
            messages.warning(request,"Recheck the Required Fields and Try Again")
        return render(request, 'customer/contact_us/contact-us.html')