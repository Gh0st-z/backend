from rest_framework import serializers
from pharmacy.models import *

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy
        fields = ('pharmacy_name', 'address', 'license_number', 'phone_number', 'pharmacy_type', 'pharmacy_logo', 'website_url')
        