from django.shortcuts import redirect, render
from django.views import View

from ads.models import Ads

# Create your views here.

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
    
    
class AdminAdsView(View):
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new ad.
        Extracts data from `request.POST` and `request.FILES`.
        """
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        url = request.POST.get('url')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Ads.objects.create(
            user_id_id=user_id,  # ForeignKey requires the ID
            title=title,
            description=description,
            image=image,
            url=url,
            start_date=start_date,
            end_date=end_date
        )

        return redirect('ads_list')  # Redirect to the list view