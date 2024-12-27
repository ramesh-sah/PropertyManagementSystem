from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Property, PropertyListingDetail, PropertyMedia, PropertyAmenities, PropertyAddress
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest


class Home(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'landing.page.html')


class AdminAddPropertyView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Extracting main property request
            agent_id = request.POST.get("agent_id")
            agent = get_object_or_404(User, user_id=agent_id)  # Adjust field if needed

            property_request = {
                "agent": agent,
                "title": request.POST.get("title"),
                "description": request.POST.get("description"),
                "category": request.POST.get("category"),
                "status": request.POST.get("status"),
                "price": request.POST.get("price"),
            }

            # Create the Property instance
            property_instance = Property.objects.create(**property_request)

            # Create related listing details
            listing_details_request = json.loads(request.POST.get("listing_details", "{}"))
            PropertyListingDetail.objects.create(
                property=property_instance,
                size=listing_details_request.get("size"),
                bedrooms=listing_details_request.get("bedrooms"),
                kitchens=listing_details_request.get("kitchens"),
                store_rooms=listing_details_request.get("store_rooms"),
                halls=listing_details_request.get("halls"),
                floors_no=listing_details_request.get("floors_no"),
            )

            # Create related property media
            media_request = json.loads(request.POST.get("media", "[]"))
            for media in media_request:
                PropertyMedia.objects.create(
                    property=property_instance,
                    image_title=media.get("image_title"),
                    image_url=media.get("image_url"),
                    video_upload=media.get("video_upload"),
                    video_title=media.get("video_title"),
                )

            # Create related property amenities
            amenities_request = json.loads(request.POST.get("amenities", "{}"))
            PropertyAmenities.objects.create(
                property=property_instance,
                ac=amenities_request.get("ac", False),
                heating=amenities_request.get("heating", False),
                garage=amenities_request.get("garage", False),
                swimming_pool=amenities_request.get("swimming_pool", False),
                parking=amenities_request.get("parking", False),
                lake_view=amenities_request.get("lake_view", False),
                garden=amenities_request.get("garden", False),
                disabled_access=amenities_request.get("disabled_access", False),
                lift=amenities_request.get("lift", False),
                pet_friendly=amenities_request.get("pet_friendly", False),
                ceiling_height=amenities_request.get("ceiling_height"),
                outdoor_shower=amenities_request.get("outdoor_shower", False),
                refrigerator=amenities_request.get("refrigerator", False),
                wifi=amenities_request.get("wifi", False),
                tv_cable=amenities_request.get("tv_cable", False),
                barbecue=amenities_request.get("barbecue", False),
                laundry_dryer=amenities_request.get("laundry_dryer", False),
                lawn=amenities_request.get("lawn", False),
                elevator=amenities_request.get("elevator", False),
            )

            # Create related property address
            address_request = json.loads(request.POST.get("address", "{}"))
            PropertyAddress.objects.create(
                property=property_instance,
                address=address_request.get("address"),
                country=address_request.get("country"),
                city=address_request.get("city"),
                zip_code=address_request.get("zip_code"),
                state=address_request.get("state"),
                latitude=address_request.get("latitude"),
                longitude=address_request.get("longitude"),
            )

            # Redirect to a success page or render a template
            return render(request, 'property/success.html', {
                'property': property_instance,
                'message': 'Property added successfully.'
            })

        except Exception as e:
            return render(request, 'property/error.html', {
                'error': str(e)
            }, status=400)
