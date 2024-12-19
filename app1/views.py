from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "property-list.html")


def propertyDetail(request):
    return render(request, "property-details.html")
