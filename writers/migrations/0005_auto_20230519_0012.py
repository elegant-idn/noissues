# Generated by Django 3.2.5 on 2023-05-19 00:12

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0004_writer_is_email_verified'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='writer',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='writer',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='following',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='is_email_verified',
        ),
        migrations.AlterField(
            model_name='writer',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
