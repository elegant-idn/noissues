# Generated by Django 4.2.5 on 2023-10-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0008_alter_writer_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='following',
        ),
        migrations.AlterField(
            model_name='writer',
            name='verification_code',
            field=models.CharField(max_length=6, verbose_name='verification_code'),
        ),
    ]
