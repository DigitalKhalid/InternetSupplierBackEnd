# Generated by Django 4.1.3 on 2022-12-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_unit_product_unit'),
        ('connection', '0012_connection_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('Connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='connection.connection', verbose_name='Connection')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='order.order', verbose_name='Order')),
                ('product', models.ManyToManyField(related_name='detials', to='product.product', verbose_name='Product')),
            ],
        ),
    ]