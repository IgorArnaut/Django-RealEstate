# Generated by Django 5.1.4 on 2024-12-12 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_remove_condition_apartment_remove_content_apartment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='numOfRooms',
            new_name='num_of_rooms',
        ),
        migrations.AlterField(
            model_name='apartment',
            name='location',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=16),
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apartments.profile')),
                ('name', models.CharField(max_length=32)),
                ('website', models.CharField(max_length=48)),
                ('email', models.EmailField(max_length=64)),
                ('registration_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=('apartments.profile',),
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apartments.profile')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=('apartments.profile',),
        ),
    ]
