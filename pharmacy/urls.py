from django.urls import path
from pharmacy.views import *

urlpatterns = [
    path('add-pharmacy/', PharmacyProfilePost, name='add-pharmacy'),
    path('get-pharmacy/', PharmacyProfileGet, name='get-pharmacy'),
]