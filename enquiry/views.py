from django.shortcuts import redirect, render
from django.views import View

from enquiry.models import Enquiry

# Create your views here.

class AdminEnquiryView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of enquiries.
        """
        enquiries = Enquiry.objects.all()
        return render(request, 'enquiry_list.html', {'enquiries': enquiries})



class CustomerEnquiryView(View):
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new enquiry.
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Optional field
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return redirect('enquiry_list')  # Redirect to the list view
    
    
    

class AgentEnquiryView(View):
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new enquiry.
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Optional field
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return redirect('enquiry_list')  # Redirect to the list view