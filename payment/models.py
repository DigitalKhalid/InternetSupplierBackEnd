from django.db import models
from customizations.choices import PaymentTypeChoice
from order.models import Order

class Payment(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    payment_type = models.CharField('Type', max_length=20, choices=PaymentTypeChoice.choices, default=PaymentTypeChoice.CREDIT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments', verbose_name='Order')
    amount = models.IntegerField('Amount', default=0)

    def __str__(self) -> str:
        return f'{self.order} Payments'