# Generated by Django 3.2.13 on 2022-04-15 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0013_addpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('plan_type', models.CharField(blank=True, max_length=255, null=True)),
                ('plan_post_number', models.CharField(blank=True, max_length=255, null=True)),
                ('plan_price', models.CharField(blank=True, max_length=255, null=True)),
                ('order_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('In Active', 'In Active')], default='In Active', max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
