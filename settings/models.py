from django.db import models

class Setting(models.Model):
    renew_order_before = models.IntegerField('Renew Order Before (Days)', default=5)
    temp_validity_extension = models.IntegerField('Temporary Validity Extension', default=5)
