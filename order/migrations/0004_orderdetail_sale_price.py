# Generated by Django 4.1.3 on 2022-12-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_connection_order_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='sale_price',
            field=models.IntegerField(default=0, verbose_name='Sale_Price'),
        ),
    ]