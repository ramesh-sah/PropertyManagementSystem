from .models import *


def properties(request):
    properties = Property.objects.all()  # Fetch all properties
    propertyamenities = PropertyAmenities.objects.all()  # Fetch all properties amenities
    propertylisiting = PropertyListingDetail.objects.all()  # Fetch all properties details
    propertymedia = PropertyMedia.objects.all()  # Fetch all properties details
    propertyaddress = PropertyAddress.objects.all()

    return {
        'properties': properties,  # Make it available in templates
        'amenities': propertyamenities,
        'listings': propertylisiting,
        'medias': propertymedia,
        'addresses': propertyaddress,

    }
