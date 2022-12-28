from django.db import models

class Setting(models.Model):
    renew_order_before = models.IntegerField('Renew Order Before (Days)', default=5)
