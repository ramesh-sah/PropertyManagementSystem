# permissions.py

from django.core.exceptions import PermissionDenied


class IsAdminUser:
    """
    Custom permission to only allow admin users to access the view.
    """

    def __call__(self, request):
        if not request.user.is_authenticated or request.user.user_type != 'admin':
            raise PermissionDenied("You do not have permission to access this page.")


class IsAgentUser:
    """
    Custom permission to only allow agent users to access the view.
    """

    def __call__(self, request):
        if not request.user.is_authenticated or request.user.user_type != 'agent':
            raise PermissionDenied("You do not have permission to access this page.")


class IsCustomerUser:
    """
    Custom permission to only allow customer users to access the view.
    """

    def __call__(self, request):
        if not request.user.is_authenticated or request.user.user_type != 'customer':
            raise PermissionDenied("You do not have permission to access this page.")
