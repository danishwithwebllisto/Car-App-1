# Generated by Django 3.2.13 on 2022-04-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_plan_plan_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='plan_post',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('Medium', 'Medium'), ('Advance', 'Advance')], default='Free', max_length=255, null=True),
        ),
    ]
