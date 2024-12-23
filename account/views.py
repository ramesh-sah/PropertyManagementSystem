from django.shortcuts import redirect, render
from django.views import View

from account.models import User

# Create your views here.


class UserRegistration(View):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display the user registration form.
        """
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new user.
        """
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        return redirect('login')  # Redirect to the login page