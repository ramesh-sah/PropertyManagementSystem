
from django.contrib import admin
from django.urls import path, include
from .views import LandingPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPage.as_view(),name='landing-page'),
    path('user/', include('account.urls'),name='account',),
    # path('ads/', include('ads.urls')),
    # path('enquiry/', include('enquiry.urls')),
    # path('organization/', include('organization.urls')),
    # path('property/', include('property.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)