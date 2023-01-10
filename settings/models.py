from django.db import models

class Setting(models.Model):
    renew_order_before = models.IntegerField('Renew Order Before (Days)', default=5)
    temp_validity_extension = models.IntegerField('Temporary Validity Extension', default=5)
    bill_auto_print = models.BooleanField('Bill Auto Print', default=True)
    order_id_prefix = models.CharField('Order ID Prefix', max_length=50, default='BizzSole')
    connection_id_prefix = models.CharField('Connection ID Prefix', max_length=50, default='BizzSole')
