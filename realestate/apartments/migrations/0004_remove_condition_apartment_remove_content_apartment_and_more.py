# Generated by Django 5.1.4 on 2024-12-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_remove_contents_apartment_condition_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='content',
            name='apartment',
        ),
        migrations.AddField(
            model_name='apartment',
            name='conditions',
            field=models.ManyToManyField(to='apartments.condition'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='contents',
            field=models.ManyToManyField(to='apartments.content'),
        ),
    ]