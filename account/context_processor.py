from .models import *


def accounts(request):
    useraddress = UserAddress.objects.all()
    usersocialmedia = UserSocialMediaProfile.objects.all()
    userdetail = User.objects.all()
    


    return {
        'useraddress': useraddress,
        'usermedia': usersocialmedia,
        'userdetail': userdetail,

    }
    

def user_profile_context(request):
    """
    Context processor to add the admin profile to the context.
    """
    if request.user.is_authenticated:
        try:
            user_profile = User.objects.get(user_id=request.user.user_id)
        except User.DoesNotExist:
            user_profile = None
    else:
        user_profile = None

    return {
        'user_profile': user_profile,
    }