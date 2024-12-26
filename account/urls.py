
from django.urls import path

from account.views import  UserDashboard, UserLogin,UserRegistration

urlpatterns = [
    path('register/',UserRegistration.as_view(),name='user-register'),
    path('login/',UserLogin.as_view(),name='user-register'),
    path('dashboard/',UserDashboard.as_view(),name='user-dashboard'),
    
    
    
   
]
