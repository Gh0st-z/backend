from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterViewPost, name='register'),
    path('login/', LoginViewPost, name='login'),
    path('register-get/', RegisterViewGet, name='login-get'),
    path('get-staff/', GetStaffDetails, name="get-staff"),
    path('get-user/', GetUserDetails, name="get-user"),
]