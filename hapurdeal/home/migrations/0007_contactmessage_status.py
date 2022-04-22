# Generated by Django 3.2.13 on 2022-04-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('Answered', 'Answered'), ('Not Answered', 'Not Answered')], default='Not Answered', max_length=255, null=True),
        ),
    ]