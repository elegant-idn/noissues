# Generated by Django 4.2.5 on 2023-10-02 01:07

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mastery_fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField()),
            ],
            options={
                'db_table': 'mastery_fields',
            },
        ),
        migrations.CreateModel(
            name='Onboarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desired_outcome', models.CharField()),
                ('success_identity', models.CharField()),
                ('success_metrics', models.CharField()),
                ('reward_options', models.CharField()),
                ('reward', models.CharField()),
                ('outcome_importance', models.CharField()),
                ('outcome_period', models.CharField()),
                ('my_reason', models.CharField()),
                ('held_back', models.CharField()),
                ('trigger_detail', models.CharField()),
                ('has_partner', models.BooleanField(default=False)),
                ('is_push_notification', models.BooleanField(default=False)),
                ('is_sms', models.BooleanField(default=False)),
                ('is_email', models.BooleanField(default=False)),
                ('partners', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None)),
                ('text5', models.CharField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'onboarding',
            },
        ),
    ]
