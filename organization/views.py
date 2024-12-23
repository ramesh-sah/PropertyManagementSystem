from django.shortcuts import redirect, render
from django.views import View

from organization.models import AboutOrganization

# Create your views here.
###about organization


class CustomerAboutOrganizationView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of AboutOrganization objects.
        Filters by `user_id` or `organization_id` if query parameters are provided.
        """
        user_id = request.GET.get('user_id')
        organization_id = request.GET.get('organization_id')

        if user_id:
            about_organizations = AboutOrganization.objects.filter(user_id=user_id)
        elif organization_id:
            about_organizations = AboutOrganization.objects.filter(organization_id=organization_id)
        else:
            about_organizations = AboutOrganization.objects.all()

        return render(request, 'customer/about.html', {
            'about_organizations': about_organizations
        })
class AdminAboutOrganizationView(View):
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new AboutOrganization object.
        Extracts data directly from `request.POST` and `request.FILES`.
        """
        user_id = request.POST.get('user_id')
        organization_id = request.POST.get('organization_id')
        overview = request.POST.get('overview')
        history = request.POST.get('history')
        core_values = request.POST.get('core_values')
        achievements = request.POST.get('achievements')
        logo = request.FILES.get('logo')
        banner_image = request.FILES.get('banner_image')

        # Create a new AboutOrganization instance
        AboutOrganization.objects.create(
            user_id_id=user_id,  # ForeignKey requires the ID
            organization_id_id=organization_id,
            overview=overview,
            history=history,
            core_values=core_values,
            achievements=achievements,
            logo=logo,
            banner_image=banner_image
        )

        return redirect('about_organization')  # Redirect to the list view
    
    
    
    

class AgentAboutOrganizationView(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of AboutOrganization objects.
        Filters by `user_id` or `organization_id` if query parameters are provided.
        """
        user_id = request.GET.get('user_id')
        organization_id = request.GET.get('organization_id')

        if user_id:
            about_organizations = AboutOrganization.objects.filter(user_id=user_id)
        elif organization_id:
            about_organizations = AboutOrganization.objects.filter(organization_id=organization_id)
        else:
            about_organizations = AboutOrganization.objects.all()

        return render(request, 'customer/about.html', {
            'about_organizations': about_organizations
        })