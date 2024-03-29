from django.db import models
from product.models import Product
from connection.models import Connection
from customizations.choices import OrderStatusChoice

class Order(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    order_id = models.CharField('Order ID', max_length=50, default=0)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name='orders', verbose_name='Connection')
    status = models.CharField('Status', max_length=20, choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING)

    def __str__(self):
        return f'{self.connection} | {self.date_created} | {self.status}'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='detials', verbose_name='Product')
    qty = models.IntegerField('Quantity', default=1)
    sale_price = models.IntegerField('Sale_Price', default=0)

    def __str__(self):
        return f'{self.product} | {self.order}'

class OrderPackageDetail(models.Model):
    package = models.OneToOneField(OrderDetail, on_delete=models.CASCADE, related_name='packagedetails', verbose_name='Package')
    valid_from = models.DateField('Valid From', null=True, blank=True) 
    valid_to = models.DateField('Valid To', null=True, blank=True)

    def __str__(self):
        return f'{self.package}'