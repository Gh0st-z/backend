from django.urls import path
from .views import RegisterViewPost, LoginViewPost, RegisterViewGet

urlpatterns = [
    path('register/', RegisterViewPost, name='register'),
    path('login/', LoginViewPost, name='login'),
    path('register-get/', RegisterViewGet, name='login-get')
]