# Generated by Django 4.2.8 on 2024-02-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('license_number', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('pharmacy_type', models.CharField(max_length=100)),
                ('pharmacy_logo', models.ImageField(upload_to='')),
                ('website_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pharmacy',
            },
        ),
    ]
