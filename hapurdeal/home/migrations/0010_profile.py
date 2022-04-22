# Generated by Django 3.2.13 on 2022-04-15 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_auto_20220414_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('business', models.CharField(blank=True, max_length=255, null=True)),
                ('area_locality', models.CharField(blank=True, max_length=255, null=True)),
                ('village_town', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
