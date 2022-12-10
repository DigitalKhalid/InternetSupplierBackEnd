from django.db import models
from product.models import Product
from connection.models import Connection
import datetime
from customizations.choices import StatusChoice, MonthChoice, YearChoices


class PackageSubscriptions(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Connection')
    package = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Package')
    month = models.PositiveSmallIntegerField('Month', choices=MonthChoice.choices)
    year = models.IntegerField('Year', choices=YearChoices.year_choices())
    activation_date = models.DateTimeField('Activation Date', auto_now=True)
    expiry_date = models.DateTimeField('Expirty Date', default=datetime.datetime.now() + datetime.timedelta(30))
    status = models.CharField('Status', max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    def __str__(self) -> str:
        return f'{self.connection} | {self.package} | {self.status}'