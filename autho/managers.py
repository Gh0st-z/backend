from autho.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class CustomerManager(BaseUserManager):
    def _create_customer(self, first_name, middle_name, last_name, email, phone_number, password):
        email = self.normalize_email(email)
        customer = self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )
        customer.set_password(password)
        customer.save(using=self._db)
        return customer
    
    def create_customer(self, first_name, middle_name, last_name, email, phone_number, password):
        return self._create_customer(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )