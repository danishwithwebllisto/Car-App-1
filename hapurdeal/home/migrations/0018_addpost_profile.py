# Generated by Django 3.2.13 on 2022-04-16 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_addpost_plan_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
