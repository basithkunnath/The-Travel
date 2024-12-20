# Generated by Django 5.1.3 on 2024-11-26 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=0, null=True, upload_to='packages_images/')),
                ('sub_image_1', models.ImageField(blank=True, null=True, upload_to='packages_images/')),
                ('sub_image_2', models.ImageField(blank=True, null=True, upload_to='packages_images/')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField(null=True)),
                ('country', models.CharField(default='Unknown Country', max_length=100)),
                ('duration', models.CharField(default='Unknown Date', max_length=100)),
                ('details_description', models.TextField(null=True)),
                ('features', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_items', to='packages.packages')),
            ],
        ),
    ]
