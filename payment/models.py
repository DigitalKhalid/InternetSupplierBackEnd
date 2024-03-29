from django.db import models
from customizations.choices import PaymentTypeChoice
from order.models import Order
from django.contrib.auth.models import User

class Payment(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    payment_type = models.CharField('Type', max_length=20, choices=PaymentTypeChoice.choices)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments', verbose_name='Order')
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_received', verbose_name='Received By')
    amount = models.IntegerField('Amount', default=0)

    def __str__(self) -> str:
        return f'{self.order} Payments'