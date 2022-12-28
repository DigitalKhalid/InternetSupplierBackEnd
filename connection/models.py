from django.db import models
from customer.models import Customer
from location.models import SubArea
from product.models import Product
import datetime
from customizations.choices import StatusChoice


class Connection(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name='connections', verbose_name='Customer')
    connection_id = models.CharField(
        'Connection ID', max_length=50, default=-1)
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE, related_name='connections', verbose_name='Sub Area')
    installation_date = models.DateField('Installation Date', default=datetime.datetime.now)
    package = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='connections', verbose_name='Package', null=True, blank=True)
    status = models.CharField('Status', max_length=20, choices=StatusChoice.choices, default=StatusChoice.INACTIVE)
    new = models.BooleanField('New Connection', default=True)
    archived = models.BooleanField('Archived', default=False)
    renewal = models.BooleanField('Renewal', default=False)

    def __str__(self) -> str:
        return f'{self.connection_id}'

    # def save(self, *args, **kw):
    #     if self.connection_id == str(-1):
    #         self.connection_id= str(f'ClickPick-{"%04d" % self.pk}')
    #     return super(Connection, self).save(*args, **kw)
