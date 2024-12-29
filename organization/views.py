from django.shortcuts import redirect, render
from django.views import View

from organization.models import AboutOrganization
from propertymanagement.permisssions import IsAdminUser, IsAgentUser, IsCustomerUser
from django.core.exceptions import PermissionDenied

# Create your views here.
# ###about organization


# class CustomerAboutOrganizationView(View):
#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests to display a list of AboutOrganization objects.
#         Filters by `user_id` or `organization_id` if query parameters are provided.
#         """
#         user_id = request.GET.get('user_id')
#         organization_id = request.GET.get('organization_id')

#         if user_id:
#             about_organizations = AboutOrganization.objects.filter(user_id=user_id)
#         elif organization_id:
#             about_organizations = AboutOrganization.objects.filter(organization_id=organization_id)
#         else:
#             about_organizations = AboutOrganization.objects.all()

#         return render(request, 'customer/about.html', {
#             'about_organizations': about_organizations
#         })


# class AgentAboutOrganizationView(View):
#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests to display a list of AboutOrganization objects.
#         Filters by `user_id` or `organization_id` if query parameters are provided.
#         """
#         user_id = request.GET.get('user_id')
#         organization_id = request.GET.get('organization_id')

#         if user_id:
#             about_organizations = AboutOrganization.objects.filter(user_id=user_id)
#         elif organization_id:
#             about_organizations = AboutOrganization.objects.filter(organization_id=organization_id)
#         else:
#             about_organizations = AboutOrganization.objects.all()

#         return render(request, 'customer/about.html', {
#             'about_organizations': about_organizations
#         })
        
class AdminOrganizationRoleView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        

        return render(request, 'admin/organization/organization-role.html')
    
class AdminOrganizationDetailView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        

        return render(request, 'admin/organization/organization-details.html')
    
class AdminOrganizationSocialMedia(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    
    def get(self, request, *args, **kwargs):
        

        return render(request, 'admin/organization/organization-social-media.html')
    
class AdminOrganizationTeamMember(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        

        return render(request, 'admin/organization/organization-team-member-add.html')
    
    
class AdminAboutOrganizationView(View):
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
        Handles GET requests to display a list of AboutOrganization objects.
        Filters by `user_id` or `organization_id` if query parameters are provided.
        """
        
        return render(request, 'admin/about_us/about_us.html')
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
    
    
    
class AdminOrganizationTermsConditionView(View):
    permission_class = IsAdminUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        return render(request, 'admin/termsConditions/terms-conditions.html')
    
    
    

class AgentOrganizationTermsConditionView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        return render(request, 'agent/termsConditions/terms-conditions.html')
    
    
    
class AgentAboutOrganizationView(View):
    permission_class = IsAgentUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of AboutOrganization objects.
        Filters by `user_id` or `organization_id` if query parameters are provided.
        """
        
        return render(request, 'agent/about_us/about_us.html')
    
    
    
    



class CustomerOrganizationTermsConditionView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/termsConditions/terms-conditions.html')
    
    
    
class CustomerAboutOrganizationView(View):
    permission_class = IsCustomerUser()  # Define the permission class

    def dispatch(self, request, *args, **kwargs):
        try:
            if self.permission_class:
                self.permission_class(request)  # Call the permission check
            return super().dispatch(request, *args, **kwargs)
        except PermissionDenied:
            return render(request, 'error/error_403.html', status=403)
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display a list of AboutOrganization objects.
        Filters by `user_id` or `organization_id` if query parameters are provided.
        """
        
        return render(request, 'customer/about_us/about_us.html')
    
    