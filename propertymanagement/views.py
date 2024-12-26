from django.shortcuts import render
from django.views import View


class LandingPage(View):
   def get(self,request,*agrs,**kwargs):
        try:
            return render(request,'landing-page.html')
        except:
            return render(request,'error.html')