from django.db import models
from pharmacy.managers import *

class Pharmacy(models.Model):
    pharmacy_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    license_number = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    pharmacy_type = models.CharField(max_length=100)
    pharmacy_logo = models.ImageField()
    website_url = models.CharField(max_length=100, null=True, blank=True)

    objects=PharmacyManager()
    USERNAME_FIELD = 'pharmacy_name'

    class Meta:
        db_table = 'pharmacy'
    
    @classmethod
    @transaction.atomic
    def create_pharmacy(self, validated_data):
        pharmacy = Pharmacy.objects.create_pharmacy(**validated_data)
        return pharmacy