# Generated by Django 4.2.5 on 2023-10-04 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0003_delete_mastery_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onboarding',
            name='text5',
        ),
    ]
