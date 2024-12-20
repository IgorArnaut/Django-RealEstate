# Generated by Django 5.1.4 on 2024-12-19 20:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_remove_agency_posted_ads_remove_landlord_posted_ads_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='landlord',
            name='username',
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='agency',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
