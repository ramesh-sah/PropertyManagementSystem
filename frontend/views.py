from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from propertymanagement.permisssions import IsAdminUser
from django.core.exceptions import PermissionDenied



class HomeView(View):
    # permission_check = IsAdminUser()

    # def dispatch(self, request, *args, **kwargs):
    #     try:
    #         self.permission_check(request)  # Call the permission check
    #     except PermissionDenied:
    #         return HttpResponse("You do not have permission to access this page.", status=403)
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "property-list.html")
    
    
    
    
def propertyDetail(request):
    return render(request, "customer/property-details.html")


def contactUs(request):
    return render(request, "customer/contactus.html")


def about(request):
    return render(request, "customer/about.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")

def addProperty(request):
    return render(request, "admin/add-property.html")
