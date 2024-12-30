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