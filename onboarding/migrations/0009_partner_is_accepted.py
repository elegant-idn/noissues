# Generated by Django 4.2.6 on 2023-10-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0008_rename_board_id_partner_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
