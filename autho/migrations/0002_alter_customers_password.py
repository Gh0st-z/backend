# Generated by Django 4.2.8 on 2023-12-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]