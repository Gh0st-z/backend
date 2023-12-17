from django.urls import path
from .views import RegisterViewPost

urlpatterns = [
    path('register/', RegisterViewPost, name='register'),
]