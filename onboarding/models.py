from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

#Create your models here.
## onboarding model
class Onboarding(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    desired_outcome = models.CharField(blank=False, null=False)
    success_identity = models.CharField(blank=False, null=False)
    success_matrics = models.CharField(blank=False, null=False)
    reward_options = models.CharField(blank=False, null=False)
    rewards = ArrayField(models.CharField(), default=[])
    outcome_importance = models.CharField(blank=False, null=False)
    outcome_period = models.CharField(blank=False, null=False)
    my_reason = models.CharField(blank=False, null=False)
    held_back = models.CharField(blank=False, null=False)
    trigger_detail = models.CharField(blank=False, null=False)
    has_partner = models.BooleanField(default=False)
    is_push_notification = models.BooleanField(default=False)
    is_sms = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    status = models.IntegerField(blank=False,default=0)
    
    class Meta:
        db_table = 'onboarding'

## partner Model

class Partner(models.Model):
    board = models.ForeignKey(Onboarding,on_delete=models.CASCADE)
    email = models.CharField(blank=False, null=False)
    access_level = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

    class Meta:
        db_table = 'partners'

## mock model
class Mock(models.Model):
    category = models.CharField(blank=False, null=False)
    choice = models.CharField(blank=False, null=False)

    class Meta:
        db_table = 'mocks'

