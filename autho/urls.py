from django.urls import path
from .views import RegisterViewPost, LoginViewPost

urlpatterns = [
    path('register/', RegisterViewPost, name='register'),
    path('login/', LoginViewPost, name='login')
]