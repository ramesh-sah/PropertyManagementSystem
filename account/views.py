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
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        usertype = request.POST.get('usertype')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # basic validations
        if not firstname or not email or not password or not confirmPassword or not lastname or not usertype:
            messages.error(request, "All fields are required")
            return redirect("account:register")

        if len(password) < 8:
            messages.error(request, "password must be at least 8 character long")
            return redirect("account:register")

        if password != confirmPassword:
            messages.error(request, "Password Do not Match")
            return redirect("account:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect("account:register")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, 'Enter a valid email address!')
            # return redirect("account:register")

        user = User(first_name=firstname, last_name=lastname, user_type=usertype, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'Your account has been created successfully!')
        # return redirect('account:login')
        return  HttpResponse("login success")

class UserLogin(View):

    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        # validate email and password

        if not email or not password:
            messages.error(request, "Both email and password fields are required")
            return redirect("account:login")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "login successfully")
            return redirect("account:register")
        else:
            # If authentication fails
            messages.error(request, "Invalid email or password")
            # return redirect("account:login")
            return  HttpResponse("login success")
class UserDashboard(View):
   
    
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'customer/dashboard/dashboard.html')
    
    
    
