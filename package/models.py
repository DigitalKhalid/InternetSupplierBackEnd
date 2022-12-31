from django.db import models
from product.models import Product
from connection.models import Connection
import datetime
from customizations.choices import StatusChoice, MonthChoice, YearChoices
from payment.models import Payment


class PackageSubscriptions(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Connection')
    package = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Package')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True, related_name='subscriptions', verbose_name='Payment')
    month = models.PositiveSmallIntegerField('Month', choices=MonthChoice.choices)
    year = models.IntegerField('Year', choices=YearChoices.year_choices())
    activation_date = models.DateField('Activation Date')
    expiry_date = models.DateField('Expirty Date')
    temp_expiry_date = models.DateField('Temp. Expirty Date', null=True, blank=True)
    status = models.CharField('Status', max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)

    def __str__(self) -> str:
        return f'{self.connection} | {self.package} | {self.status}'