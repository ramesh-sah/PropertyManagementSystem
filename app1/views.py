from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "property-list.html")


def propertyDetail(request):
    return render(request, "customer/property-details.html")


def contactUs(request):
    return render(request, "customer/contactus.html")


def about(request):
    return render(request, "customer/about.html")
