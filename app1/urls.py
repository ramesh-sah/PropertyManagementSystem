from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property-detail', views.propertyDetail, name='property-detail'),
    path('contact-us', views.contactUs, name='contact-us'),
    path('about', views.about, name='about'),

]
