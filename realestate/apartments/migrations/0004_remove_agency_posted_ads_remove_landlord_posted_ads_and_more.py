# Generated by Django 5.1.4 on 2024-12-19 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_alter_ad_date_posted_alter_agency_registration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='posted_ads',
        ),
        migrations.RemoveField(
            model_name='landlord',
            name='posted_ads',
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2024, 12, 19, 19, 30, 41, 316252, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='agency',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 19, 19, 30, 41, 317267, tzinfo=datetime.timezone.utc)),
        ),
    ]