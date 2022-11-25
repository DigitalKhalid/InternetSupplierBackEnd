from django.db import models
from customer.models import Customer
import datetime

class Connection(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name='connections', verbose_name='Customer')
    connection_id = models.CharField(
        'Connection ID', max_length=50, default=-1)
    installation_date = models.DateField('Installation Date', default=datetime.datetime.now)
    package = models.CharField('Package', max_length=25, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.customer} Connection'

    def save(self, *args, **kw):
        if self.connection_id == str(-1):
            self.connection_id= str(f'ClickPick-{"%04d" % self.pk}')
        return super(Connection, self).save(*args, **kw)
