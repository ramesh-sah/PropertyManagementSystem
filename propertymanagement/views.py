from django.shortcuts import render
from django.views import View       
from django.shortcuts import render
from django.http import Http404
from propertymanagement.permisssions import IsAdminUser
from django.contrib import messages


class LandingPage(View):
   
   def get(self,request,*agrs,**kwargs):
        try:
            # messages.success(request, "Landing Page")
            return render(request,'landing-page.html')
        except:
            return render(request,'error/error_404.html')
        
        

class Custom400Error(View):
    def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'error/error_400.html')
        except:
            return render(request,'error/error_400.html')
        


class Custom403Error(View):
    def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'error/error_403.html')
        except:
            return render(request,'error/error_403.html')
        
class Custom404Error(View):
    def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'error/error_404.html')
        except:
            return render(request,'error/error_404.html')
    
    
class Custom500Error(View):
    def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'error/error_500.html')
        except:
            return render(request,'error/error_500.html')
    
class Custom503Error(View):
    def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'error/error_503.html')
        except:
            return render(request,'error/error_404.html')
        
        
