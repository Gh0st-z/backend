import datetime
import os
import uuid
from django.db import models
from autho.models import User

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Pharmacy(models.Model):
    pharmacy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pharmacy_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    license_number = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    pharmacy_type = models.CharField(max_length=100)
    pharmacy_logo = models.ImageField(upload_to=filepath, null=True, blank=True)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    admin_id = models.OneToOneField(User, on_delete=models.CASCADE)

    USERNAME_FIELD = 'pharmacy_name'

    class Meta:
        db_table = 'pharmacy'

    def __str__(self):
        return str(self.id)

    @classmethod
    @transaction.atomic
    def create_pharmacy(self, validated_data):
        pharmacy = Pharmacy.objects.create_pharmacy(**validated_data)
        return pharmacy
