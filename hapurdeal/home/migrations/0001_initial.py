# Generated by Django 3.2.13 on 2022-04-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteInfo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('subheading', models.CharField(blank=True, max_length=255, null=True)),
                ('des', models.TextField(blank=True, null=True)),
                ('fb', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]