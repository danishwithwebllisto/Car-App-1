# Generated by Django 3.2.13 on 2022-04-21 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='user',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.RemoveField(
            model_name='addpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='store_photo',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
