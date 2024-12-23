from django.urls import path
from .views import register
from . import views

app_name = "account"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]
