# Generated by Django 4.1.3 on 2022-12-31 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_balance_remove_order_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPackageDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField(verbose_name='Valid From')),
                ('valid_to', models.DateField(verbose_name='Valid To')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='order.orderdetail', verbose_name='Order Package')),
            ],
        ),
    ]
