from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404

from propertymanagement.permisssions import IsAdminUser, IsAgentUser, IsCustomerUser
from .models import Property, PropertyListingDetail, PropertyMedia, PropertyAmenities, PropertyAddress, PropertyCoupon
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from decimal import Decimal


# admin views
class AdminPropertyAddView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/property/add-property.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        status = request.POST.get('status')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        country = request.POST.get('country')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        coupon_code = request.POST.get('coupon')
        percentage = request.POST.get('percentage')
        valid_from = request.POST.get('valid_from')
        valid_until = request.POST.get('valid_until')

        # Retrieve additional features (checkboxes)
        additional_features = request.POST.getlist('feature')  # This will return a list of selected features

        # Create Property instance
        property_instance = Property.objects.create(
            agent=request.user,  # Assuming the logged-in user is an agent
            title=title,
            status=status,
            category=category,
            description=description,
            price=Decimal(price) if price else None,
        )

        # PropertyListingDetail data (No need to repeat property data here)
        area = request.POST.get('area')
        bedroom = request.POST.get('bedroom')
        kitchen = request.POST.get('kitchen')
        storeroom = request.POST.get('storeroom')
        halls = request.POST.get('halls')
        floor = request.POST.get('floor')
        bathroom = request.POST.get('bathroom')

        # Create PropertyListingDetail instance
        PropertyListingDetail.objects.create(
            property=property_instance,
            size=area,
            bedrooms=bedroom,
            kitchens=kitchen,
            store_rooms=storeroom,
            halls=halls,
            floors_no=floor
        )

        # PropertyMedia (Images and Videos)
        images = request.FILES.getlist('images')  # Multiple image uploads
        video = request.FILES.get('video')  # Single video upload

        if images:
            for image in images:
                PropertyMedia.objects.create(
                    property=property_instance,
                    image=image
                )

        if video:
            PropertyMedia.objects.create(
                property=property_instance,
                video=video
            )

        # PropertyAmenities (Features)
        amenities_data = {
            'ac': 'ac' in request.POST,
            'heating': 'heating' in request.POST,
            'garage': 'garage' in request.POST,
            'swimming_pool': 'swimming_pool' in request.POST,
            'parking': 'parking' in request.POST,
            'lake_view': 'lake_view' in request.POST,
            'garden': 'garden' in request.POST,
            'disabled_access': 'disabled_access' in request.POST,
            'lift': 'lift' in request.POST,
            'pet_friendly': 'pet_friendly' in request.POST,
            'ceiling_height': request.POST.get('ceiling_height'),
            'outdoor_shower': 'outdoor_shower' in request.POST,
            'refrigerator': 'refrigerator' in request.POST,
            'wifi': 'wifi' in request.POST,
            'tv_cable': 'tv_cable' in request.POST,
            'barbecue': 'barbecue' in request.POST,
            'laundry_dryer': 'laundry_dryer' in request.POST,
            'lawn': 'lawn' in request.POST,
            'elevator': 'elevator' in request.POST,
        }

        PropertyAmenities.objects.create(property=property_instance, **amenities_data)

        # PropertyAddress data
        address_data = {
            'property': property_instance,
            'address': address,
            'country': country,
            'zip_code': zipcode,
            'city': city,
            'state': state,
            'latitude': latitude,
            'longitude': longitude,
        }
        PropertyAddress.objects.create(**address_data)

        # PropertyCoupon (Discounts)
        # if coupon_code:
        #     PropertyCoupon.objects.create(
        #         property=property_instance,
        #         code=coupon_code,
        #         coupon_type=request.POST.get('coupon_type'),
        #         discount_amount=request.POST.get('discount_amount'),
        #         discount_percentage=percentage,
        #         valid_from=valid_from,
        #         valid_until=valid_until
        #     )

        return render(request, 'admin/property/add-property.html')


class AdminPropertyListView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/property/property-list.html')


class AdminPropertyEnquiryView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/property/property-enquiry.html')


class AdminPropertyDetailView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/property/property-details.html')


class AdminPropertyCouponAddView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/propertyCoupon/add-coupon.html')


class AdminPropertyCouponListView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/propertyCoupon/list-coupon.html')


class AdminPropertyCouponUpdateView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'admin/propertyCoupon/update-coupon.html')


## Agent Views


class AgentPropertyAddView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/property/add-property.html')


class AgentPropertyListView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/property/property-list.html')


class AgentPropertyEnquiryView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/property/property-enquiry.html')


class AgentPropertyDetailView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/property/property-details.html')


class AgentPropertyCouponAddView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/propertyCoupon/add-coupon.html')


class AgentPropertyCouponListView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/propertyCoupon/list-coupon.html')


class AgentPropertyCouponUpdateView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'agent/propertyCoupon/update-coupon.html')


class CustomerPropertyListView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/property/property-list.html')


class CustomerPropertyDetailView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/property/property-details.html')


class CustomerPropertyEnquiryView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/property/property-enquiry.html')
