from django.shortcuts import redirect, render
from django.views import View
from django.core.paginator import Paginator
from ads.models import Ads
from propertymanagement.permisssions import IsAdminUser
from django.core.exceptions import PermissionDenied

# Create your views here.


    
    
class AdminAddAdsView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display the form to create a new ad.
        """
        return render(request, 'admin/ads/add-ads.html')
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new ad.
        Extracts data from `request.POST` and `request.FILES`.
        """
        user = request.user
        title = request.POST.get('ads_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        url = request.POST.get('url')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Ads.objects.create(
            user=user,# ForeignKey requires the ID
            title=title,
            description=description,
            image=image,
            url=url,
            start_date=start_date,
            end_date=end_date
        )

        return redirect('ads:admin-ads-add')  # Redirect to the list view
    
    
class AdminAdsListView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads with pagination.
        """
        # Fetch all ads, ordered by newest first
        ads = Ads.objects.all().order_by('-created_at')
        
        # Apply filters based on query parameters
        title = request.GET.get('title')  # e.g., "Active", "Inactive"
        status = request.GET.get('status')  # e.g., "YYYY-MM-DD"
        # end_date = request.GET.get('end_date')  # e.g., "YYYY-MM-DD"
        print(title)
        
        
        
        # Pagination setup
        page_number = request.GET.get('page', 1)  # Default to the first page
        paginator = Paginator(ads, 10)  # Show 10 ads per page
        
        # Get the page object for the current page
        page_obj = paginator.get_page(page_number)
        
        # Render the template with the ads for the current page
        return render(request, 'admin/ads/list-ads.html', {'ads': page_obj})
    
class AgentAdsView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        Filters by `user_id` if provided in query parameters.
        """
        user_id = request.GET.get('user_id')

        if user_id:
            ads = Ads.objects.filter(user_id=user_id)
        else:
            ads = Ads.objects.all()

        return render(request, 'ads_list.html', {'ads': ads})
    
    
    
class CustomerAdsView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of ads.
        Filters by `user_id` if provided in query parameters.
        """
        user_id = request.GET.get('user_id')

        if user_id:
            ads = Ads.objects.filter(user_id=user_id)
        else:
            ads = Ads.objects.all()

        return render(request, 'ads_list.html', {'ads': ads})

