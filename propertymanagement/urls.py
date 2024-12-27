
from django.contrib import admin
from django.urls import path, include
from .views import LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPage.as_view(),name='landing-page'),
    path('user/', include('account.urls',namespace='account')),
    path('ads/', include('ads.urls',namespace='ads')),
    path('contact/', include('contact_us.urls',namespace='contact_us')),
    path('organization/', include('organization.urls',namespace='organization')),
    path('property/', include('property.urls',namespace='property')),
]
