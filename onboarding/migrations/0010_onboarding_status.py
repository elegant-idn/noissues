# Generated by Django 4.2.6 on 2023-10-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0009_partner_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='onboarding',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
