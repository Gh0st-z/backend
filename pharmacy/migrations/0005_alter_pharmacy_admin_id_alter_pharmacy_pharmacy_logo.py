# Generated by Django 4.2.8 on 2024-03-04 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharmacy', '0004_alter_pharmacy_pharmacy_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='admin_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
