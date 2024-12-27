from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from account.models import User

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import re
from django.contrib.auth import get_user_model, authenticate, login
from django.views import View

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
        print(user.last_name, user.first_name, user.user_type)

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

    
    
class AdminDashboard(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/dashboard/dashboard.html')
    
    
    
class AdminAddAgentView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/agents/add-agent.html')
    
    
class AdminListAgentView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/agents/list-agent.html')
    
class AdminDetailAgentView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/agents/agent-profile.html')
    
    
    
class AdminAddCustomerView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/customer/add-customer.html')
    
    
class AdminListCustomerView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/customer/list-customer.html')
class AdminDetailCustomerView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/customer/customer-profile.html')
    
class AdminProfileView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'admin/admin-profile/view-profile.html')
    
    
    
class AgentDashboard(View):
   
    def get(self,request,*args,**kwargs):
        
        return render(request,'agent/dashboard/dashboard.html')
    
class AgentProfileView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'agent/agent-profile/view-profile.html')
    

class UserDashboard(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'customer/dashboard/dashboard.html')
    
    
class CustomerProfileView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'customer/customer-profile/view-profile.html')
    
    