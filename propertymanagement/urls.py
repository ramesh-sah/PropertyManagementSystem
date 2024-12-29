
from django.contrib import admin
from django.urls import path, include

from .views import Custom400Error, Custom403Error, Custom404Error, Custom500Error, Custom503Error
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

handler400 = Custom400Error.as_view()
handler403 = Custom403Error.as_view()
handler404 = Custom404Error.as_view()
handler500 = Custom500Error.as_view()
handler503 = Custom503Error.as_view()