# Generated by Django 4.2.8 on 2024-03-04 11:02

from django.db import migrations, models
import pharmacy.models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_alter_pharmacy_admin_id_alter_pharmacy_pharmacy_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_logo',
            field=models.ImageField(blank=True, null=True, upload_to=pharmacy.models.filepath),
        ),
    ]
