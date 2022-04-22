# Generated by Django 3.2.13 on 2022-04-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220414_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.TextField(blank=True, null=True)),
                ('address2', models.TextField(blank=True, null=True)),
                ('googlemap', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
