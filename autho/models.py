from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from autho.managers import UserManager

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10)
    role = models.CharField(max_length=10)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = 'user'

    @classmethod
    @transaction.atomic
    def create_user(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
