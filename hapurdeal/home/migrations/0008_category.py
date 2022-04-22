# Generated by Django 3.2.13 on 2022-04-14 12:37

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contactmessage_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('status', models.CharField(blank=True, choices=[('Add To Home', 'Add To Home'), ('Normal', 'Normal')], default='Normal\t', max_length=255, null=True)),
            ],
        ),
    ]