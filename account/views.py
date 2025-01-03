import time
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from account.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import User, UserSocialMediaProfile, UserAddress

from .models import  UserSocialMediaProfile, UserAddress





# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import re
from django.contrib.auth import get_user_model, authenticate, login
from django.views import View

from propertymanagement.permisssions import IsAdminUser, IsAgentUser, IsCustomerUser

# Create your views here.

User = get_user_model()


class UserRegistration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        # Retrieve data from the POST request
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # print(firstname, lastname, user_type, email, password, confirm_password)

        # basic validations
        if not firstname or not email or not password or not confirm_password or not lastname or not user_type:
            messages.error(request, "All fields are required")
            return redirect("account:user-register")

        if len(password) < 8:
            messages.error(request, "password must be at least 8 character long")
            return redirect("account:user-register")

        if password != confirm_password:
            messages.error(request, "Password Do not Match")
            return redirect("account:user-register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect("account:user-register")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, 'Enter a valid email address!')
            return redirect("account:user-register")

        user = User(first_name=firstname, last_name=lastname, user_type=user_type, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'Your account has been created successfully!')
        return redirect('account:user-login')
        
        
       

class UserLogin(View):

    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
        

    
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)

        # validate email and password
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            # print("invalid email")
            
            return redirect("account:user-login")

        if not email or not password:
            messages.error(request, "Both email and password fields are required")
            return redirect("account:user-login")
            print("Both fileds are reqired")

        user = authenticate(request, email=email, password=password)
        

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            

            if user.user_type == 'admin':
                return redirect("account:admin-dashboard")
            elif user.user_type == 'agent':
                return redirect("account:agent-dashboard")
            elif user.user_type == 'customer':
                return redirect("account:user-dashboard")
            else:
                return redirect("account:user-register")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("account:user-login")
        




class UserLogout(View):

    def get(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            logout(request)  # Logs out the user
            messages.success(request, "You have been logged out successfully.")
        else:
            messages.warning(request, "You are not logged in.")
        
        return redirect('account:user-login')  # Redirect to the login page or any other page

    
class AdminDashboard(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/dashboard/dashboard.html')
    
    
    
class AdminAddAgentView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/agents/add-agent.html')
        
    def post(self, request, *args, **kwargs):
        # Get the form data from the request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profile_picture= request.FILES.get('profile_picture')
        password = request.POST.get('password')
        
        # Social Media URLs from the form
        social_media_facebook = request.POST.get('social_media_facebook')
        social_media_whatsapp = request.POST.get('social_media_whatsapp')
        social_media_instagram = request.POST.get('social_media_instagram')
        social_media_linkedin = request.POST.get('social_media_linkedin')
        
        # Social Media URL fields from the form
        social_media_url_facebook = request.POST.get('social_media_url_facebook')
        social_media_url_whatsapp = request.POST.get('social_media_url_whatsapp')
        social_media_url_instagram = request.POST.get('social_media_url_instagram')
        social_media_url_linkedin = request.POST.get('social_media_url_linkedin')
        
        # Address information from the form
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        state = request.POST.get('state')
        
        user_type = 'agent'
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('account:admin-add-agent')
        
        # Create User instance
        user = User(first_name=first_name, last_name=last_name, user_type=user_type, email=email,phone_number=phone_number,profile_picture=profile_picture)
        user.set_password(password)
        user.save()
        
        # Create Social Media Profiles for the user based on form data
        if social_media_facebook and social_media_url_facebook:
            UserSocialMediaProfile.objects.create(user=user, platform='facebook', url=social_media_url_facebook)
        if social_media_whatsapp and social_media_url_whatsapp:
            UserSocialMediaProfile.objects.create(user=user, platform='whatsApp', url=social_media_url_whatsapp)
        if social_media_instagram and social_media_url_instagram:
            UserSocialMediaProfile.objects.create(user=user, platform='instagram', url=social_media_url_instagram)
        if social_media_linkedin and social_media_url_linkedin:
            UserSocialMediaProfile.objects.create(user=user, platform='linkedin', url=social_media_url_linkedin)
        
        # Create User Address instance
        UserAddress.objects.create(
            user=user,
            address=address,
            country=country,
            city=city,
            zip_code=zip_code,
            state=state
        )
        print(first_name, last_name, email, phone_number, profile_picture, password, social_media_facebook, social_media_whatsapp, social_media_instagram, social_media_linkedin, social_media_url_facebook, social_media_url_whatsapp, social_media_url_instagram, social_media_url_linkedin, address, country, city, zip_code, state)
        # Return success message or redirect as needed
        messages.success(request, "User and related data saved successfully!")
        return redirect('account:admin-list-agent')

            
    
    
class AdminListAgentView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
   
    def get(self, request, *args, **kwargs):
        # Fetch the agent list and associated data
        agentList = User.objects.filter(user_type='agent').order_by('-created_at')
        agentSocialMedia = UserSocialMediaProfile.objects.filter(user__user_type='agent')
        agentAddresses = UserAddress.objects.filter(user__user_type='agent')

        # Set up pagination for agentList
        paginator = Paginator(agentList, 15)  # Show 6 agents per page
        page_number = request.GET.get('page')  # Get the current page number from query params
        page_obj = paginator.get_page(page_number)  # Get the page object

        # Prepare context for rendering
        context = {
            'page_obj': page_obj,  # Pass the paginated agent list
            'agentSocialMedia': agentSocialMedia,
            'agentAddresses': agentAddresses,
        }
        
        # Render the page with the paginated context
        return render(request, 'admin/agents/list-agent.html', context)

    
class AdminDetailAgentView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,user_id=None,*args,**kwargs):
        agent=User.objects.get(user_id=user_id)
        agentSocialMedia = UserSocialMediaProfile.objects.filter(user=agent)
        agentAddresses = UserAddress.objects.filter(user=agent)
        context={
            'agent':agent,
            'agentSocialMedia':agentSocialMedia,
            'agentAddresses':agentAddresses
        }
        
        
        return render(request,'admin/agents/agent-profile.html',context)
    
    
    
class AdminAddCustomerView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/customer/add-customer.html')
    
    def post(self, request, *args, **kwargs):
        # Get the form data from the request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profile_picture= request.FILES.get('profile_picture')
        password = request.POST.get('password')
        
        # Social Media URLs from the form
        social_media_facebook = request.POST.get('social_media_facebook')
        social_media_whatsapp = request.POST.get('social_media_whatsapp')
        social_media_instagram = request.POST.get('social_media_instagram')
        social_media_linkedin = request.POST.get('social_media_linkedin')
        
        # Social Media URL fields from the form
        social_media_url_facebook = request.POST.get('social_media_url_facebook')
        social_media_url_whatsapp = request.POST.get('social_media_url_whatsapp')
        social_media_url_instagram = request.POST.get('social_media_url_instagram')
        social_media_url_linkedin = request.POST.get('social_media_url_linkedin')
        
        # Address information from the form
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        state = request.POST.get('state')
        
        user_type = 'customer'
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('account:admin-add-agent')
        
        # Create User instance
        user = User(first_name=first_name, last_name=last_name, user_type=user_type, email=email,phone_number=phone_number,profile_picture=profile_picture)
        user.set_password(password)
        user.save()
        
        # Create Social Media Profiles for the user based on form data
        if social_media_facebook and social_media_url_facebook:
            UserSocialMediaProfile.objects.create(user=user, platform='facebook', url=social_media_url_facebook)
        if social_media_whatsapp and social_media_url_whatsapp:
            UserSocialMediaProfile.objects.create(user=user, platform='whatsApp', url=social_media_url_whatsapp)
        if social_media_instagram and social_media_url_instagram:
            UserSocialMediaProfile.objects.create(user=user, platform='instagram', url=social_media_url_instagram)
        if social_media_linkedin and social_media_url_linkedin:
            UserSocialMediaProfile.objects.create(user=user, platform='linkedin', url=social_media_url_linkedin)
        
        # Create User Address instance
        UserAddress.objects.create(
            user=user,
            address=address,
            country=country,
            city=city,
            zip_code=zip_code,
            state=state
        )
        print(first_name, last_name, email, phone_number, profile_picture, password, social_media_facebook, social_media_whatsapp, social_media_instagram, social_media_linkedin, social_media_url_facebook, social_media_url_whatsapp, social_media_url_instagram, social_media_url_linkedin, address, country, city, zip_code, state)
        # Return success message or redirect as needed
        messages.success(request, "User and related data saved successfully!")
        return redirect('account:admin-list-customer')

            
    
    
class AdminListCustomerView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self, request, *args, **kwargs):
        # Fetch the agent list and associated data
        customerList = User.objects.filter(user_type='customer')

        customerSocialMedia = UserSocialMediaProfile.objects.filter(user__user_type='customer')
        customerAddresses = UserAddress.objects.filter(user__user_type='customer')

        # Set up pagination for agentList
        paginator = Paginator(customerList, 15)  # Show 6 agents per page
        page_number = request.GET.get('page')  # Get the current page number from query params
        page_obj = paginator.get_page(page_number)  # Get the page object

        # Prepare context for rendering
        context = {
            'page_obj': page_obj,  # Pass the paginated agent list
            'customerSocialMedia': customerSocialMedia,
            'customerAddresses': customerAddresses,
        }
        
        # Render the page with the paginated context
        return render(request, 'admin/customer/list-customer.html', context)
        
        
class AdminDetailCustomerView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/customer/customer-profile.html')
    
class AdminProfileView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,*args,**kwargs):
        user=request.user
        admin_profile=User.objects.get(user_id=user.user_id)
        return render(request,'admin/admin-profile/view-profile.html',{'admin_profile':admin_profile})
    
    
    
class AgentDashboard(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
   
    def get(self,request,*args,**kwargs):
        
        return render(request,'agent/dashboard/dashboard.html')
    
class AgentProfileView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
   
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'agent/agent-profile/view-profile.html')
    

class UserDashboard(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        # try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        # except PermissionDenied:
        #     return render(request, 'error/error_403.html', status=403)
   
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'customer/dashboard/dashboard.html')
    
    
class CustomerProfileView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'customer/customer-profile/view-profile.html')
    
    