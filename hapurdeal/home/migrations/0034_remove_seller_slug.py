# Generated by Django 3.2.13 on 2022-04-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_seller_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='slug',
        ),
    ]
