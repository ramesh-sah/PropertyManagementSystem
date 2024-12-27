
from django.urls import path

from .views import AdminAddAdsView,AdminAdsListView

app_name='ads'
urlpatterns = [
    
    path('admin-ads-add/',AdminAddAdsView.as_view(),name='admin-ads-add'),
    path('admin-ads-list/',AdminAdsListView.as_view(),name='admin-ads-list'),
    
]
