# Generated by Django 5.1.4 on 2024-12-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_rename_username_agency_name_remove_landlord_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='email',
            field=models.EmailField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='email',
            field=models.EmailField(max_length=64, null=True),
        ),
    ]
