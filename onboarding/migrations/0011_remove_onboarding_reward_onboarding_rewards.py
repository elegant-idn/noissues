# Generated by Django 4.2.6 on 2023-10-23 19:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0010_onboarding_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onboarding',
            name='reward',
        ),
        migrations.AddField(
            model_name='onboarding',
            name='rewards',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), default=[], size=None),
        ),
    ]
