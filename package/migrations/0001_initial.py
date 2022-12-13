# Generated by Django 4.1.3 on 2022-12-10 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0008_alter_product_purchase_price_and_more'),
        ('connection', '0019_alter_connection_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('activation_date', models.DateTimeField(auto_now=True, verbose_name='Activation Date')),
                ('Expiry_date', models.DateTimeField(auto_now=True, verbose_name='Expirty Date')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20, verbose_name='Status')),
                ('Connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='connection.connection', verbose_name='Connection')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='product.product', verbose_name='Package')),
            ],
        ),
    ]