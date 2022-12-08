from django.db import models
from product.models import Product
from connection.models import Connection

class Order(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    Connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name='orders', verbose_name='Connection')

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', verbose_name='Order')
    product = models.ManyToManyField(Product, related_name='detials', verbose_name='Product')
    qty = models.IntegerField('Quantity', default=1)