# Generated by Django 3.2.13 on 2022-04-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20220421_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
