from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from autho.managers import CustomerManager

class customers(AbstractBaseUser):
    customer_id = models.BigAutoField(primary_key=True, default=None)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    objects = CustomerManager()
    class Meta:
        db_table = 'customers'